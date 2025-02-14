import json
from typing import Any


class ProductFile:
    def __init__(self, path: str):
        self._path = path

    def scan(self) -> dict[str, Any]:
        with open(self._path, 'r') as file:
            return json.load(file)
