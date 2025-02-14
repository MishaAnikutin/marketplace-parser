from dataclasses import dataclass
from typing import Union, List

from entities.ProductFile import ProductFile


@dataclass
class Filter:
    name: str
    key: str
    value: str
    mapped_value: Union[str, int]


class Product:
    name: str

    def __init__(self, name: str, filters: List[Filter]):
        self.name = name
        self._filters = filters

    @classmethod
    def from_file(cls, product_file: ProductFile):
        json_data = product_file.scan()

        return cls(
            name=json_data['name'],
            filters=[Filter(**el) for el in json_data['filters']]
        )

    @property
    def filters(self) -> list[Filter]:
        return self._filters
