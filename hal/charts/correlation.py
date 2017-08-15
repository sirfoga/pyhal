# !/usr/bin/python3
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
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

    pyplot.gcf().subplots_adjust(bottom=0.25)  # include xlabels
