import json
import uuid

from typing import Awaitable
from typing import Optional
import tornado.web

from consts.consts import CrawlData
from consts.consts import Status
from db.sql import SQL
from redis_queue import queue
from tasks.process_task import process


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def initialize(self):
        self.db = SQL()
        self.queue = queue

    def on_finish(self):
        self.db.close()


def get_handlers():
    """ The application calls this to get all the handlers from this module """
    return [
        (r"/api/ingest/?", IngestHandler),
        (r"/api/status/(.+)/?", StatusHandler),
    ]


class IngestHandler(BaseHandler):
    def post(self):
        url = self.get_body_argument("url")
        notify_channel_types = self.get_body_argument("notify_at")
        notify_channels = self.get_body_argument("notify_to")
        crawl_id = uuid.uuid4().hex
        data = {
            "crawl_id": crawl_id,
            "url": url,
            "channel_types": notify_channel_types,
            "channels": notify_channels,
            "status": Status.ACCEPTED,
        }
        self.db.add(data)
        self.queue.enqueue(process, crawl_id)
        self.set_status(202)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"id": crawl_id}))


class StatusHandler(BaseHandler):
    def get(self, _id: str):
        data = self.db.get(_id)
        if not data:
            data = (Status.NOT_FOUND,)

        self.set_status(200)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"status": data[CrawlData.STATUS]}))
