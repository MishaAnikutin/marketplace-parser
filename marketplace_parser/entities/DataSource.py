import requests
from retry import retry
from fake_useragent import UserAgent

from entities import Query


class DataSource:
    def __init__(self, query: Query):
        self._url = query.build()
        self._headers = {"User-Agent": UserAgent().random}

    @retry(Exception, tries=3, delay=5)
    def scrap(self) -> dict:
        response = requests.get(url=self._url, headers=self._headers)

        response.raise_for_status()

        return response.json()['data']['products']