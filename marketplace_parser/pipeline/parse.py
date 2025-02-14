import requests
from typing import Iterable
from fake_useragent import UserAgent

from pipe import Pipe


def parse_one(url: str) -> dict:
    response = requests.get(url=url, headers={"User-Agent": UserAgent().random})

    response.raise_for_status()

    return response.json()['data']['products']


@Pipe
def parse(iterable: Iterable):
    return ((name, parse_one(url)) for name, url in iterable)
