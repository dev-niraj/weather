import os
import csv
from collections import namedtuple

data = []

Record = namedtuple(
    'Record',
    'date,actual_mean_temp,actual_min_temp,actual_max_temp,average_min_temp,'
    'average_max_temp,record_min_temp,record_max_temp,record_min_temp_year,'
    'record_max_temp_year,actual_precipitation,average_precipitation,record_precipitation'
)


def init():
    base = os.path.dirname(__file__)
    filename = os.path.abspath('data/seattle.txt')

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            row = parse_row(row)
            print(type(row.get('actual_precipitation')),
                  row.get('actual_precipitation'))


def parse_row(row):
    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])
    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])
    
    r = Record(
        **row
    )

    return row
