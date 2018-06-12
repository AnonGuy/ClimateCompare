"""Main data analysis functionality."""

import numpy

from parsing import towns


def _town_values(data, index):
    """Get the statistics calculations of a town's values."""
    values = [datum[index] for datum in data]
    mean = round(numpy.mean(values), 2)
    median = round(numpy.median(values), 2)
    deviation = round(numpy.std(values), 2)
    q75, q25 = numpy.percentile(values, (75, 25))
    interquartile_range = round(q75 - q25, 2)
    return values, mean, median, deviation, interquartile_range


def display_data(town, measurement, units, index):
    """Display calculations to the user, including outliers."""
    town = town.title()
    values, mean, median, std, iqr = _town_values(data, index)
    print(f'{town}\'s mean {measurement}: {mean} {units}')
    print(f'{town}\'s median {measurement}: {median} {units}')
    print(f'{town}\'s standard deviation in {measurement}: {std} {units}')
    print(f'{town}\'s interquartile range in {measurement}: {iqr} {units}')
    for value in values:
        if abs(value - mean) > 2 * std:
            print(f'• Outlier found: {value} {units}')
    print()

# Calculate mean, standard deviation, median and interquartile range.
for town, data in towns.items():
    town = town.title()
    display_data(town, 'temperature', '°C', 1)
    display_data(town, 'wind speed', 'kn', 2)
