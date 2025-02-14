import os
from celery import Celery
from celery.schedules import crontab

from pipeline import open_files, to_filters, to_queries, parse, to_csv


app = Celery('parser', broker='redis://redis:6379/0')


@app.task
def parse_and_save_data():
    (
        os.listdir('products')
        | open_files
        | to_filters
        | to_queries
        | parse
        | to_csv
    )


app.conf.beat_schedule = {
    'parse-twice-a-day': {
        'task': 'tasks.parse_and_save_data',
        'schedule': crontab(hour=8, minute=0),
    },
}
