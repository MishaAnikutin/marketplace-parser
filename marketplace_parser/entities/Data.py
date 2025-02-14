from datetime import datetime

import pandas as pd

from .DataSource import DataSource


class Data:
    def __init__(self, name: str, data: pd.DataFrame):
        self._name = name
        self._data = data

    @classmethod
    def from_source(cls, name: str, data_source: DataSource):
        data = pd.DataFrame(data_source.scrap())

        return cls(name, data)

    def save(self):
        today = datetime.now().strftime('%Y-%m-%d')

        self._data.to_csv(f'data/{today}_{self._name}.csv', index=False)
