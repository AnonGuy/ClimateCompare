"""Reading and parsing CSV data."""

import csv

from datetime import datetime


# Define dictionary of climate data
towns = {
    'cambourne': None,
    'heathrow': None,
    'leuchars': None
}

# Read CSV data and apply dictionary values
for town in towns:
    with open(f'data/{town}.csv') as file:
        reader = csv.reader(file)
        towns[town] = list(reader)

# Change string dates to datetime objects, and values to floats
for town, data in towns.items():
    for i, datum in enumerate(data):
        datum[0] = datetime.strptime(datum[0], '%d/%m/%Y')
        datum[1], datum[2] = map(
            float, (datum[1], datum[2])
        )
        data[i] = datum
    towns[town] = data

# Remove anomalous date from sampled data
anomaly = datetime(2015, 6, 2)
for town, data in towns.items():
    data = [n for n in data if anomaly not in n]
    towns[town] = data
