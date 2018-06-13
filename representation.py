"""Main script to display plotted data."""

from parsing import towns
from plot_scripts import box_plot, histogram

box_plot.plot(towns)
histogram.plot(towns)
