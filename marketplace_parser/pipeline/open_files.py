import json
from typing import Iterable

from pipe import Pipe


def open_one(path):
    with open(path, 'r') as file:
        return json.load(file)

@Pipe
def open_files(iterable: Iterable) -> list[dict]:
    return (
        (name, open_one(f'products/{name}'))
        for name in iterable
    )
