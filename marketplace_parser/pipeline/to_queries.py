from typing import Iterable
from urllib.parse import urlencode

from pipe import Pipe

from .to_filters import Filter


def to_query(filters: list[Filter]):
    url = 'https://search.wb.ru/exactmatch/ru/common/v9/search?'

    default_params = {
        'ab_testid': 'pers_norm_no_boost',
        'appType': 1,
        'curr': 'rub',
        'dest': -1255987,
        'lang': 'ru',
        'resultset': 'catalog',
        'frating': 1,
        'spp': 30,
        'suppressSpellcheck': False
    }

    for product_filter in filters:
        default_params[product_filter.key] = product_filter.mapped_value

    return url + urlencode(default_params)


@Pipe
def to_queries(iterable: Iterable):
    return (
        (name, to_query(product_filters))
        for name, product_filters in iterable
    )
