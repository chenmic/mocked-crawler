from consts.consts import CrawlData
from consts.consts import Status
from db.sql import SQL
from db.elastic import MockedElasticsearch
from logic.crawl_logic.crawl import CrawlLogic
from redis_queue import queue
from tasks.notify_task import notify


def process(crawl_id: str):
    with SQL() as sql:
        crawl_data = sql.get(crawl_id)
        sql.update_status(crawl_id, Status.RUNNING)
        url = crawl_data[CrawlData.URL]

        try:
            crawl_logic = CrawlLogic()
            html = crawl_logic.crawl(url)
            elastic = MockedElasticsearch()
            elastic.add(crawl_id, html)
            sql.update_status(crawl_id, Status.COMPLETE)
            queue.enqueue(notify, crawl_id)
        except Exception as e:
            print(e)
            sql.update_status(crawl_id, Status.ERROR)
