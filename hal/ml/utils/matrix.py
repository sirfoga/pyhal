#!/usr/bin/env python
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Functions to deal with matrices. """

import numpy as np


def precision(matrix):
    """ Calculates accuracy on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    true_pos = matrix[0][0]
    false_pos = matrix[1][0]

    try:
        return 1.0 * true_pos / (true_pos + false_pos)
    except:  # division by 0
        return 0


def recall(matrix):
    """ Calculates recall on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    true_pos = matrix[0][0]
    false_neg = matrix[0][1]

    try:
        return 1.0 * true_pos / (true_pos + false_neg)
    except:  # division by 0
        return 0


def true_neg_rate(matrix):
    """ Calculates true negative rate on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    false_pos = matrix[1][0]
    true_neg = matrix[1][1]

    try:
        return 1.0 * true_neg / (true_neg + false_pos)
    except:  # division by 0
        return 0


def accuracy(matrix):
    """ Calculates recall on database

    :param matrix: 2x2 matrix that looks like
    True Positive  - False Negative
         |         -       |
    False Positive - True Negative
    """

    true_pos = matrix[0][0]
    false_pos = matrix[1][0]
    false_neg = matrix[0][1]
    true_neg = matrix[1][1]

    try:
        return \
            1.0 * (true_pos + true_neg) / (true_pos + true_neg + false_pos +
                                           false_neg)
    except:  # division by 0
        return 0


def f1_score(matrix):
    """ Calculates f1 score on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    m_pre = precision(matrix)
    rec = recall(matrix)

    try:
        return 2.0 / (1.0 / m_pre + 1.0 / rec)  # harmonic mean
    except:  # division by 0
        return 0


def get_column_of_matrix(column_index, matrix):
    """
    :param column_index: int >= 0
        Column index to take
    :param matrix: [] of []
        Matrix
    :return: []
        Column of array at position given
    """

    try:
        np_matrix = np.array(matrix)
        np_column = np_matrix[:, column_index]
        return list(np_column)
    except:
        return []


def get_subset_of_matrix(headers_to_sample, all_headers, data):
    """
    :param headers_to_sample: [] of str
        List of columns to get
    :param all_headers: [] of str
        List of all headers in matrix
    :param data: [] of []
        Matrix of float values
    :return: [] of []
        Correlation matrix of selected columns
    """

    header_to_column = {}  # create index of headers
    for header in all_headers:
        header_to_column[header] = all_headers.index(header)

    subset_columns = []
    for header in headers_to_sample:
        header_ind = header_to_column[header]  # index of header
        header_column = get_column_of_matrix(header_ind, data)

        for i, value in enumerate(header_column):
            header_column[i] = float(value)  # get float

        subset_columns.append(header_column)

    return np.transpose(subset_columns)


def remove_column_from_matrix(headers, header_to_remove, data):
    """
    :param headers: [] of str
        Column names
    :param header_to_remove: str
        Name of column to remove
    :param data: matrix ([] of [])
        Data
    :return: headers, data
        Headers without header removed and data without column removed
    """

    column_index_to_remove = headers.index(header_to_remove)
    new_data = np.delete(data, column_index_to_remove, 1)  # remove column
    new_headers = headers  # copy headers
    new_headers.remove(header_to_remove)  # remove date header
    return new_headers, new_data


def add_columns_to_matrix(headers, data, new_headers, new_columns):
    """
    :param headers: headers: [] of str
        Column names
    :param data: matrix ([] of [])
        Data
    :param new_headers: [] of str
        Names of new columns
    :param new_columns: ([] of [])
        New columns to add
    :return: headers, data
        New headers (with new headers) and data with new columns
    """

    new_data = []  # add each column
    for i, row in range(len(data)):
        new_row = []
        for col in row:
            new_row.append(col)  # add old columns

        for new_col in new_columns[i]:
            new_row.append(new_col)  # add new columns
        new_data.append(new_row)  # add new row

    new_column_names = headers + new_headers
    return new_column_names, new_data
