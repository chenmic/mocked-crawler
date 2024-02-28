from consts.consts import CrawlData
from db.sql import SQL
from logic.notification_logic.notify import NotificationLogic


def notify(crawl_id: str):
    with SQL() as sql:
        crawl_data = sql.get(crawl_id)
        channel_types = crawl_data[CrawlData.CHANNEL_TYPES].split()
        channels = crawl_data[CrawlData.CHANNELS].split()
        notification_logic = NotificationLogic()
        notification_logic.notify(channel_types, channels)
