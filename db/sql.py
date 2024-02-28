from contextlib import closing
import sqlite3


class SQL:
    def __init__(self):
        self.connection = sqlite3.connect("crawler.db")
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS crawls (crawl_id TEXT, url TEXT, channel_types TEXT, channels TEXT, status TEXT)")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def add(self, data: dict):
        to_add = tuple(data.values())
        skeleton = ", ".join(["?" for _ in to_add])
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(f"INSERT INTO crawls VALUES ({skeleton})", to_add)
        self.connection.commit()

    def get(self, _id: str) -> tuple:
        with closing(self.connection.cursor()) as cursor:
            return cursor.execute("SELECT * FROM crawls WHERE crawl_id = ?", (_id,)).fetchone()

    def update_status(self, _id: str, status: str):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute("UPDATE crawls SET status = ? WHERE crawl_id = ?", (status, _id))
        self.connection.commit()

    def close(self):
        self.connection.close()
