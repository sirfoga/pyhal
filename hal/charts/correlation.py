# !/usr/bin/python3
# coding: utf-8


""" Everything you need to create correlation charts """

import numpy as np
from matplotlib import pyplot as plt, cm

from hal.charts.models import SimpleChart


def create_correlation_matrix_plot(correlation_matrix, title, feature_list):
    """
    :param correlation_matrix: [] of []
        Correlation matrix of features
    :param title: str
        Title of plot
    :param feature_list: [] of str
        List of names of features
    :return: void
        shows the given correlation matrix as image
    """

    chart = SimpleChart(title)
    ax1 = chart.create()

    ax1.set_xticks(list(range(len(feature_list))))
    ax1.set_xticklabels([feature_list[i] for i in range(len(feature_list))],
                        rotation=90)
    ax1.set_yticks(list(range(len(feature_list))))
    ax1.set_yticklabels([feature_list[i] for i in range(len(feature_list))])
    cax = ax1.imshow(correlation_matrix, interpolation="nearest",
                     cmap=cm.get_cmap("jet", 30))
    chart.get_fig().colorbar(cax, ticks=np.linspace(-1, 1, 21))

    plt.gcf().subplots_adjust(bottom=0.25)  # include x-labels
