# !/usr/bin/python3
# coding: utf-8

""" Correlate values in arrays producing fancy good-looking matrices """

import os

import numpy as np
from matplotlib import pyplot

from hal.charts import correlation as cr_plot
from hal.files.models import Document, FileSystem
from hal.files.parsers import parse_csv_file
from hal.ml.utils.matrix import get_column_of_matrix
from time import time


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

    cr_plot.create_correlation_matrix_plot(correlation_matrix, title,
                                           feature_list)
    pyplot.show()


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

        for i, value in enumerate(header_column):
            header_column[i] = float(value)  # get float

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

    correlation_matrix = get_correlation_matrix_of_columns(headers_to_test,
                                                           headers, data)
    show_correlation_matrix(correlation_matrix, title, headers_to_test)
    pyplot.show()


def save_correlation_matrix_of_columns(title, headers_to_test, headers, data,
                                       out_file):
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

    correlation_matrix = get_correlation_matrix_of_columns(headers_to_test,
                                                           headers, data)
    cr_plot.create_correlation_matrix_plot(correlation_matrix, title,
                                           headers_to_test)

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

    output_folder = os.path.join(folder_path,
                                 "output-" + str(int(time())))
    os.makedirs(output_folder)  # make necessary folders to create directory

    for file in FileSystem.list_content(folder_path, False, False):
        if os.path.isfile(file) and str(file).endswith("csv"):
            print("Analysing file ", str(file))

            file_name = Document(file).name.strip()
            output_file_name = file_name + ".png"  # save output as image
            output_file_path = os.path.join(output_folder, output_file_name)

            try:
                headers, data = parse_csv_file(file)  # parse raw data
                save_correlation_matrix_of_columns(
                    "Correlation of logs data for file " + file_name, headers,
                    headers,
                    data, output_file_path)
            except:
                print("Cannot save correlation matrix of file \"", str(file),
                      "\"")
