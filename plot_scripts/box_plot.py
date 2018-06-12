"""Generate a Box plot from town data."""

import numpy
import matplotlib.pyplot as plt


def format_values(towns, index):
    """Take "towns" dictionary and convert to a plottable format."""
    standard = []
    outliers = []

    for data in towns.values():
        values = [datum[index] for datum in data]
        mean = numpy.mean(values)
        range_limit = numpy.std(values) * 2
        outliers.append(
            [
                datum[index] for datum in data
                if abs(mean - datum[index]) > range_limit
            ]
        )
        standard.append(
            [
                datum[index] for datum in data
                if abs(mean - datum[index]) <= range_limit
            ]
        )

    return standard, outliers


def plot(towns):
    """Plot the given "towns" dictionary."""
    plt.clf()
    fig, ax = plt.subplots()
    fig.suptitle(
        'Daily mean temperature at three UK towns (2015)',
        fontsize=14, fontweight='bold'
    )
    ax.set_ylabel('Daily Mean Temperature (°C)')
    ax.set_title('Cambourne, Heathrow and Leuchars')
    standard, outliers = format_values(towns, 1)
    ax.boxplot(standard)
    ax.set_xticklabels(('Cambourne', 'Heathrow', 'Leuchars'))
    plt.savefig('images/box_plot/temperature.png', dpi=300)
    plt.clf()
    fig, ax = plt.subplots()
    fig.suptitle(
        'Daily mean windspeed at three UK towns (2015)',
        fontsize=14, fontweight='bold'
    )
    ax.set_ylabel('Daily Mean Windspeed (kn)')
    ax.set_title('Cambourne, Heathrow and Leuchars')
    standard, outliers = format_values(towns, 2)
    ax.boxplot(standard)
    ax.set_xticklabels(('Cambourne', 'Heathrow', 'Leuchars'))
    plt.savefig('images/box_plot/windspeed.png', dpi=300)
