# !/usr/bin/python3
# coding: utf-8


""" Everything you need to create correlation charts """

import numpy as np
from matplotlib import pyplot, cm


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

    fig = pyplot.figure()
    ax1 = fig.add_subplot(111)
    ax1.grid(True)
    pyplot.title(title)

    ax1.set_xticks(list(range(len(feature_list))))
    ax1.set_xticklabels([feature_list[i] for i in range(len(feature_list))],
                        rotation=90)
    ax1.set_yticks(list(range(len(feature_list))))
    ax1.set_yticklabels([feature_list[i] for i in range(len(feature_list))])
    cax = ax1.imshow(correlation_matrix, interpolation="nearest",
                     cmap=cm.get_cmap("jet", 30))
    fig.colorbar(cax, ticks=np.linspace(-1, 1, 21))

    pyplot.gcf().subplots_adjust(bottom=0.25)  # include x-labels
