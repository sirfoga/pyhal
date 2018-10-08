# -*- coding: utf-8 -*-

""" Create easily bar charts """

import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt

from hal.charts.models import SimpleChart
from hal.data.lists import normalize_array


def setup_chart(title, bottom=None):
    """
    Setups chart

    Args:
        title: Title of chart
        bottom: Bottom margin (Default value = None)

    Returns:
        axis: Chart axis
    """
    chart = SimpleChart(title)
    if bottom:
        chart.setup(bottom)

    return chart.create()


def create_bar_chart(title, x_labels, y_values, y_label):
    """
    Creates bar char

    # Args:
        title: Title of chart
        x_labels: Names for each variable
        y_values: Values of x labels
        y_label: Label of y axis

    # Returns:
        chart: Bar chart
    """
    ax1 = setup_chart(title, bottom=0.25)
    ax1.set_xticks(list(range(len(x_labels))))
    ax1.set_xticklabels([x_labels[i] for i in range(len(x_labels))],
                        rotation=90)
    plt.ylabel(y_label)

    x_pos = range(len(x_labels))
    plt.bar(x_pos, y_values, align="center")

    return ax1


def create_multiple_bar_chart(title, x_labels, mul_y_values, mul_y_labels,
                              normalize=False):
    """
    Creates bar chart with multiple lines

    Args:
        title: Title of chart
        x_labels: Names for each variable
        mul_y_values: list of values of x labels
        mul_y_labels: list of labels for each y value
        normalize: True iff you want to normalize each y series

    # Returns
        chart: Bar chart
    """
    ax1 = setup_chart(title)
    ax1.set_xticks(list(range(len(x_labels))))
    ax1.set_xticklabels([x_labels[i] for i in range(len(x_labels))],
                        rotation=90)

    y_counts = len(mul_y_values)
    colors = cm.rainbow(np.linspace(0, 1, y_counts))  # different colors
    max_bar_width = 0.6
    bar_width = max_bar_width / y_counts  # width of each bar
    x_shifts = np.linspace(0, max_bar_width,
                           y_counts) - max_bar_width * 0.5  # center in 0
    ax_series = []
    for i in range(y_counts):
        x_pos = range(len(x_labels))  # x points
        x_pos = np.array(x_pos) + x_shifts[i]  # shift for each y series
        if normalize:  # normalize array
            y_values = normalize_array(mul_y_values[i]),
        else:
            y_values = mul_y_values[i],

        ax_series.append(
            ax1.bar(
                x_pos,
                y_values,
                width=bar_width,
                align="center",
                color=colors[i]
            )
        )

    ax1.legend(ax_series, mul_y_labels)

    return ax1


def create_sym_log_bar_chart(title, x_labels, y_values, y_label):
    """
    Creates bar chart (log version)

    Args:
        title: Title of chart
        x_labels: Names for each variable
        y_values: Values of x labels
        y_label: Label of y axis

    # Returns
        chart: Sym-log bar chart
    """
    ax1 = create_bar_chart(title, x_labels, y_values, y_label)
    ax1.set_yscale("sym-log", linthreshy=1e-12)  # logarithmic plot
    return ax1
