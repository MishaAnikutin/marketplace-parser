import pandas as pd
from typing import Iterable
from datetime import datetime

from pipe import Pipe


@Pipe
def to_csv(iterable: Iterable):
    for name, data in iterable:
        today = datetime.now().strftime('%Y-%m-%d')

        pd.DataFrame(data).to_csv(f'data/{today}_{name}.csv', index=False)

