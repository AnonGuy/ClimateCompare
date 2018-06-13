"""Generate a Histogram from town data."""

import numpy
import matplotlib.pyplot as plt


def format_values(towns, town, index):
    """Take "towns" dictionary and convert to a plottable format."""
    standard = []
    outliers = []
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
    values = [datum[index] for datum in towns[town]]
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
    standard, outliers = format_values(towns, 'cambourne', 1)
    n, bins, patches = plt.hist(
        standard, 50, normed=1, facecolor='green', alpha=0.75
    )
    plt.xticks(range(1, 11), [
        '9 - 10', '10 - 11', '11 - 12', '12 - 13', '13 - 14', '14 - 15',
        '15 - 16', '16 - 17', '17 - 18'
    ], rotation=15)
    plt.savefig('images/histogram/cambourne/temperature.png', dpi=300)
