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

import os
import time

import numpy as np
from matplotlib import pyplot, cm

from hal.files.models import Document, FileSystem
from hal.ml.data.parser import parse_csv_file
from hal.ml.utils.matrix import get_column_of_matrix


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
    pyplot.gcf().subplots_adjust(bottom=0.25)  # include xlabels

    ax1.set_xticks(list(range(len(feature_list))))
    ax1.set_xticklabels([feature_list[i] for i in range(len(feature_list))], rotation=90)
    ax1.set_yticks(list(range(len(feature_list))))
    ax1.set_yticklabels([feature_list[i] for i in range(len(feature_list))])
    cax = ax1.imshow(correlation_matrix, interpolation="nearest", cmap=cm.get_cmap("jet", 30))
    fig.colorbar(cax, ticks=[.5, .55, .6, .65, .7, .75, .8, .85, .90, .95, 1])  # add colorbar

    pyplot.gcf().subplots_adjust(bottom=0.25)  # include xlabels
    pyplot.show()


def create_visual_correlation_matrix(correlation_matrix, title, feature_list):
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
    ax1.set_xticklabels([feature_list[i] for i in range(len(feature_list))], rotation=90)
    ax1.set_yticks(list(range(len(feature_list))))
    ax1.set_yticklabels([feature_list[i] for i in range(len(feature_list))])
    cax = ax1.imshow(correlation_matrix, interpolation="nearest", cmap=cm.get_cmap("jet", 30))
    fig.colorbar(cax, ticks=np.linspace(-1, 1, 21))

    pyplot.gcf().subplots_adjust(bottom=0.25)  # include xlabels


def get_correlation_matrix_of_columns(headers_to_test, headers, data):
    """
    :param headers_to_test: [] of str
        List of columns to get correlation matrix of
    :param headers: [] of str
        List of all headers in matrix
    :param data: [] of []
        Matrix of float values
    :return: [] of []
        Correlation matrix of selected columns
    """

    header_to_column = {}  # create index of headers
    for header in headers:
        header_to_column[header] = headers.index(header)

    data_to_test = []
    for header in headers_to_test:
        header_column = get_column_of_matrix(header_to_column[header], data)

        for i in range(len(header_column)):
            header_column[i] = float(header_column[i])  # get float

        data_to_test.append(header_column)

    return get_correlation_matrix(data_to_test)


def show_correlation_matrix_of_columns(title, headers_to_test, headers, data):
    """
    :param title: str
        Title to show
    :param headers_to_test: [] of str
        List of columns to get correlation matrix of
    :param headers: [] of str
        List of all headers in matrix
    :param data: [] of []
        Matrix of float values
    :return: void
        Shows on screen correlation matrix of selected headers
    """

    correlation_matrix = get_correlation_matrix_of_columns(headers_to_test, headers, data)
    show_correlation_matrix(correlation_matrix, title, headers_to_test)
    pyplot.show()


def save_correlation_matrix_of_columns(title, headers_to_test, headers, data, out_file):
    """
    :param title: str
        Title to show
    :param headers_to_test: [] of str
        List of columns to get correlation matrix of
    :param headers: [] of str
        List of all headers in matrix
    :param data: [] of []
        Matrix of float values
    :param out_file: str
        Output file
    :return: void
        Saves correlation matrix of selected headers
    """

    correlation_matrix = get_correlation_matrix_of_columns(headers_to_test, headers, data)
    create_visual_correlation_matrix(correlation_matrix, title, headers_to_test)

    fig = pyplot.gcf()  # get reference to figure
    fig.set_size_inches(23.4, 23.4)
    pyplot.savefig(out_file, dpi=120)


def save_correlation_matrix_of_data_files_in_folder(folder_path):
    """
    :param folder_path: str
        Folder containing logs data
    :return: void
        Saves each file's correlation matrix of common headers
    """

    output_folder = os.path.join(folder_path, "output-" + str(int(time.time())))
    os.makedirs(output_folder)  # make necessary folders to create directory

    for f in FileSystem.ls(folder_path, False, False):
        if os.path.isfile(f) and str(f).endswith("csv"):
            print("Analysing file ", str(f))

            file_name = Document(f).name.strip()
            output_file_name = file_name + ".png"  # save output as image
            output_file_path = os.path.join(output_folder, output_file_name)

            try:
                headers, data = parse_csv_file(f)  # parse raw data
                save_correlation_matrix_of_columns("Correlation of logs data for file " + file_name, headers, headers,
                                                   data, output_file_path)
            except Exception as e:
                print("Cannot save correlation matrix of file \"", str(f), "\" because of")
                print(str(e))
