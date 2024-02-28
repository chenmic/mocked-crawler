import requests


class CrawlLogic:
    def crawl(self, url: str) -> str:
        response = requests.get(url, timeout=10)
        return response.text
