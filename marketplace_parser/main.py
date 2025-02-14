import os
from celery import Celery
from celery.schedules import crontab

from entities import Query, Product, DataSource, ProductFile, Data

app = Celery('parser', broker='redis://redis:6379/0')


@app.task
def parse_and_save_data():
    for path in os.listdir('products'):
        name = path.split()[0]

        Data.from_source(
            name=name,
            data_source=DataSource(Query(Product.from_file(ProductFile(f'products/{path}')))),
        ).save()


app.conf.beat_schedule = {
    'parse-twice-a-day': {
        'task': 'tasks.parse_and_save_data',
        'schedule': crontab(hour=8, minute=0),
    },
}
