import os
from pipeline import open_files, to_filters, to_queries, parse, to_csv


(
    os.listdir('products')
    | open_files
    | to_filters
    | to_queries
    | parse
    | to_csv
)
