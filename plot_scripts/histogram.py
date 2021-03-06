"""Generate a Histogram from town data."""

import numpy
import matplotlib.pyplot as plt


def format_values(towns, town, index, intervals):
    """Take "towns" dictionary and convert to a plottable format."""
    standard = []
    outliers = []
    values = [
        datum[index] for datum in towns[town]
    ]
    std = numpy.std(values)
    mean = numpy.mean(values)
    for datum in towns[town]:
        if abs(mean - datum[index]) <= std * 2:
            for (low, high), value in intervals.items():
                if low <= datum[index] < high:
                    standard.append(value)
                    break
        else:
            outliers.append(datum[index])

    return standard, outliers


def plot(towns):
    """Plot the given "towns" dictionary."""
    plt.clf()
    fig, ax = plt.subplots()
    fig.suptitle(
        'Daily mean temperature in Cambourne (2015)',
        fontsize=14, fontweight='bold'
    )
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Daily Mean Temperature (°C)')
    ax.set_title('Cambourne')
    intervals = {
        (9, 10): 1,
        (10, 11): 2,
        (11, 12): 3,
        (12, 13): 4,
        (13, 14): 5,
        (14, 15): 6,
        (15, 16): 7,
        (16, 17): 8,
        (17, 18): 9,
        (18, 19): 10
    }
    standard, outliers = format_values(towns, 'cambourne', 1, intervals)
    n, bins, patches = plt.hist(
        standard, 50, normed=1, facecolor='green', alpha=0.75
    )
    plt.xticks(range(1, 11), [
        '9 - 10', '10 - 11', '11 - 12', '12 - 13', '13 - 14', '14 - 15',
        '15 - 16', '16 - 17', '17 - 18', '18 - 19'
    ], rotation=15)
    plt.savefig('images/histogram/cambourne/temperature.png', dpi=300)

    plt.clf()
    fig, ax = plt.subplots()
    fig.suptitle(
        'Daily mean windspeed in Cambourne (2015)',
        fontsize=14, fontweight='bold'
    )
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Daily Mean Windspeed (kn)')
    ax.set_title('Cambourne')
    intervals = {
        (6, 7): 1,
        (7, 8): 2,
        (8, 9): 3,
        (9, 10): 4,
        (10, 11): 5,
        (11, 12): 6,
        (12, 13): 7,
        (13, 14): 8,
        (14, 15): 9
    }
    standard, outliers = format_values(towns, 'cambourne', 2, intervals)
    n, bins, patches = plt.hist(
        standard, 50, normed=1, facecolor='green', alpha=0.75
    )
    plt.xticks(range(1, 11), [
        '6 - 7', '7 - 8', '8 - 9', '9 - 10', '10 - 11', '11 - 12',
        '12 - 13', '13 - 14', '14 - 15', '15 - 16'
    ], rotation=15)
    plt.savefig('images/histogram/cambourne/windspeed.png', dpi=300)

    plt.clf()
    fig, ax = plt.subplots()
    fig.suptitle(
        'Daily mean temperature in Heathrow (2015)',
        fontsize=14, fontweight='bold'
    )
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Daily Mean Temperature (°C)')
    ax.set_title('Heathrow')
    intervals = {
        (9, 10): 1,
        (10, 11): 2,
        (11, 12): 3,
        (12, 13): 4,
        (13, 14): 5,
        (14, 15): 6,
        (15, 16): 7,
        (16, 17): 8,
        (17, 18): 9,
        (18, 19): 10,
        (19, 20): 11
    }
    standard, outliers = format_values(towns, 'heathrow', 1, intervals)
    n, bins, patches = plt.hist(
        standard, 50, normed=1, facecolor='green', alpha=0.75
    )
    plt.xticks(range(1, 12), [
        '9 - 10', '10 - 11', '11 - 12', '12 - 13', '13 - 14', '14 - 15',
        '15 - 16', '16 - 17', '17 - 18', '18 - 19', '19 - 20'
    ], rotation=20, fontsize=8)
    plt.savefig('images/histogram/heathrow/temperature.png', dpi=300)

    plt.clf()
    fig, ax = plt.subplots()
    fig.suptitle(
        'Daily mean windspeed in Heathrow (2015)',
        fontsize=14, fontweight='bold'
    )
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Daily Mean Windspeed (kn)')
    ax.set_title('Heathrow')
    intervals = {
        (4, 5): 1,
        (5, 6): 2,
        (6, 7): 3,
        (7, 8): 4,
        (8, 9): 5,
        (9, 10): 6,
        (10, 11): 7,
        (11, 12): 8,
        (12, 13): 9,
        (13, 14): 10,
        (14, 15): 11,
        (15, 16): 12,
        (16, 17): 13,
        (17, 18): 14,
        (18, 19): 15
    }
    standard, outliers = format_values(towns, 'heathrow', 2, intervals)
    n, bins, patches = plt.hist(
        standard, 50, normed=1, facecolor='green', alpha=0.75
    )
    plt.xticks(range(1, 9), [
        '4 - 5', '5 - 6', '6 - 7', '7 - 8', '8 - 9', '9 - 10', '10 - 11',
        '11 - 12'
    ], rotation=20, fontsize=8)
    plt.savefig('images/histogram/heathrow/windspeed.png', dpi=300)

    plt.clf()
    fig, ax = plt.subplots()
    fig.suptitle(
        'Daily mean temperature in Leuchars (2015)',
        fontsize=14, fontweight='bold'
    )
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Daily Mean Temperature (°C)')
    ax.set_title('Leuchars')
    intervals = {
        (9, 10): 1,
        (10, 11): 2,
        (11, 12): 3,
        (12, 13): 4,
        (13, 14): 5,
        (14, 15): 6,
        (15, 16): 7,
        (16, 17): 8
    }
    standard, outliers = format_values(towns, 'leuchars', 1, intervals)
    n, bins, patches = plt.hist(
        standard, 50, normed=1, facecolor='green', alpha=0.75
    )
    plt.xticks(range(1, 9), [
        '9 - 10', '10 - 11', '11 - 12', '12 - 13', '13 - 14', '14 - 15',
        '15 - 16', '16 - 17'
    ], rotation=20, fontsize=8)
    plt.savefig('images/histogram/leuchars/temperature.png', dpi=300)

    plt.clf()
    fig, ax = plt.subplots()
    fig.suptitle(
        'Daily mean windspeed in Leuchars (2015)',
        fontsize=14, fontweight='bold'
    )
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Daily Mean Windspeed (kn)')
    ax.set_title('Leuchars')
    intervals = {
        (9, 10): 1,
        (10, 11): 2,
        (11, 12): 3,
        (12, 13): 4,
        (13, 14): 5,
        (14, 15): 6,
        (15, 16): 7,
        (16, 17): 8
    }
    standard, outliers = format_values(towns, 'leuchars', 1, intervals)
    n, bins, patches = plt.hist(
        standard, 50, normed=1, facecolor='green', alpha=0.75
    )
    plt.xticks(range(1, 9), [
        '9 - 10', '10 - 11', '11 - 12', '12 - 13', '13 - 14', '14 - 15',
        '15 - 16', '16 - 17'
    ], rotation=20, fontsize=8)
    plt.savefig('images/histogram/leuchars/windspeed.png', dpi=300)
