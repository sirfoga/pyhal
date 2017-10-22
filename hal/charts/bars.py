# !/usr/bin/python3
# coding: utf-8

# Copyright 2016-2018 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Create easily bar charts """

import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt

from hal.ml.utils.misc import normalize_array


def create_bar_chart(title, x_labels, y_values, y_label):
    """
    :param title: str
        Title of chart
    :param x_labels: [] of str
        Names for each variable
    :param y_values: [] of float
        Values of x labels
    :param y_label: str
        Label of y axis
    :return: Subplot
        Bar chart
    """

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.title(title)
    plt.grid(True)
    plt.gcf().subplots_adjust(bottom=0.25)  # include long x-labels

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
    :param title: str
        Title of chart
    :param x_labels: [] of str
        Names for each variable
    :param mul_y_values: [] of [] of float
        List of values of x labels
    :param mul_y_labels: [] of str
        List of labels for each y value
    :param normalize: bool
        True iff you want to normalize each y series
    :return: Subplot
        Bar chart
    """

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.title(title)
    plt.grid(True)
    plt.gcf().subplots_adjust(bottom=0.25)  # include long x-labels

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
    :param title: str
        Title of chart
    :param x_labels: [] of str
        Names for each variable
    :param y_values: [] of float
        Values of x labels
    :param y_label: str
        Label of y axis
    :return: return
        Sym-log bar chart
    """

    ax1 = create_bar_chart(title, x_labels, y_values, y_label)
    ax1.set_yscale("sym-log", linthreshy=1e-12)  # logarithmic plot
    return ax1
