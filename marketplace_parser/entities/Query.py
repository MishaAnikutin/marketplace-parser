from urllib.parse import urlencode

from .Product import Product


class Query:
    _url = 'https://search.wb.ru/exactmatch/ru/common/v9/search?'

    _default_params = {
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

    def __init__(self, product: Product):
        self._product = product

    def build(self):
        for product_filter in self._product.filters:
            self._default_params[product_filter.key] = product_filter.mapped_value

        return self._url + urlencode(self._default_params)
