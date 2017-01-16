#!/usr/bin/env python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
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


""" Various tools and utilities to deal with database and machine learning. """


import numpy as np
from matplotlib import pyplot, cm


def precision(matrix):
    """ Calcualtes accuarcy on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    tp = matrix[0][0]
    fp = matrix[1][0]

    try:
        return 1.0 * tp / (tp + fp)
    except Exception:  # division by 0
        return 0


def recall(matrix):
    """ Calcualtes recall on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    tp = matrix[0][0]
    fn = matrix[0][1]

    try:
        return 1.0 * tp / (tp + fn)
    except Exception:  # division by 0
        return 0


def tn_rate(matrix):
    """ Calcualtes true negative rate on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    fp = matrix[1][0]
    tn = matrix[1][1]

    try:
        return 1.0 * tn / (tn + fp)
    except Exception:  # division by 0
        return 0


def accuracy(matrix):
    """ Calcualtes recall on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    tp = matrix[0][0]
    fp = matrix[1][0]
    fn = matrix[0][1]
    tn = matrix[1][1]

    try:
        return 1.0 * (tp + tn) / (tp + tn + fp + fn)
    except Exception:  # division by 0
        return 0


def f1_score(matrix):
    """ Calcualtes f1 score on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    p = precision(matrix)
    r = recall(matrix)

    try:
        return 2.0 / (1.0 / p + 1.0 / r)  # harmonic mean
    except Exception:  # division by 0
        return 0


def pearson(x, y):
    """ Pearson coefficient of arrays"""

    return np.corrcoef(x, y)[0][1]


def get_correlation_matrix(matrix):
    """
    :param matrix: [] of []
        List of features to get correlation matrix
    :return: [] of []
        correlation matrix
    """

    return np.corrcoef(matrix)


def show_correlation_matrix(correlation_matrix, title, feature_list):
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
    ax1.set_yticks(list(range(len(feature_list))))
    ax1.set_yticklabels([feature_list[i] + " : " + str(i) for i in range(len(feature_list))])
    cmap = cm.get_cmap("jet", 30)
    cax = ax1.imshow(correlation_matrix, interpolation="nearest", cmap=cmap)
    fig.colorbar(cax, ticks=[.5, .55, .6, .65, .7, .75, .8, .85, .90, .95, 1])  # add colorbar
    pyplot.show()
