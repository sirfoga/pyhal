#!/usr/bin/env python
# coding: utf-8

""" Functions to deal with matrices. """

import numpy as np


def precision(matrix):
    """
    :param matrix: 2 x 2 matrix
        True positives are in [0,0], true negatives are in [1,1],
        false negatives are in [0,1] and false positives are in [1,0]
    :return: float
        Calculates accuracy on database
    """

    true_pos = matrix[0][0]
    false_pos = matrix[1][0]

    try:
        return 1.0 * true_pos / (true_pos + false_pos)
    except:  # division by 0
        return 0


def recall(matrix):
    """
    :param matrix: 2 x 2 matrix
        True positives are in [0,0], true negatives are in [1,1],
        false negatives are in [0,1] and false positives are in [1,0]
    :return: float
        Calculates recall on database
    """

    true_pos = matrix[0][0]
    false_neg = matrix[0][1]

    try:
        return 1.0 * true_pos / (true_pos + false_neg)
    except:  # division by 0
        return 0


def true_neg_rate(matrix):
    """
    :param matrix: 2 x 2 matrix
        True positives are in [0,0], true negatives are in [1,1],
        false negatives are in [0,1] and false positives are in [1,0]
    :return: float
        Calculates true negative rate on database
    """

    false_pos = matrix[1][0]
    true_neg = matrix[1][1]

    try:
        return 1.0 * true_neg / (true_neg + false_pos)
    except:  # division by 0
        return 0


def accuracy(matrix):
    """
    :param matrix: 2 x 2 matrix
        True positives are in [0,0], true negatives are in [1,1],
        false negatives are in [0,1] and false positives are in [1,0]
    :return: float
        Calculates accuracy on database
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
    """
    :param matrix: 2 x 2 matrix
        True positives are in [0,0], true negatives are in [1,1],
        false negatives are in [0,1] and false positives are in [1,0]
    :return: float
        Calculates F1 score on database
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
