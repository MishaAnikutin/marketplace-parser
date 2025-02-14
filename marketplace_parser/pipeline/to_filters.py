from dataclasses import dataclass
from typing import Union, Iterable

from pipe import Pipe


@dataclass
class Filter:
    name: str
    key: str
    value: str
    mapped_value: Union[str, int]


@Pipe
def to_filters(iterable: Iterable):
    return (
        (name, [Filter(**el) for el in product['filters']])
        for name, product in iterable
    )
