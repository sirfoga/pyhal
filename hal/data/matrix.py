#!/usr/bin/env python
# coding: utf-8

""" Functions to deal with matrices """

import numpy as np
from sklearn.preprocessing import LabelEncoder


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def precision(self):
        """
        :return: float
            Calculates accuracy on database
        """

        true_pos = self.matrix[0][0]
        false_pos = self.matrix[1][0]

        try:
            return 1.0 * true_pos / (true_pos + false_pos)
        except:  # division by 0
            return 0

    def recall(self):
        """
        :return: float
            Calculates recall on database
        """

        true_pos = self.matrix[0][0]
        false_neg = self.matrix[0][1]

        try:
            return 1.0 * true_pos / (true_pos + false_neg)
        except:  # division by 0
            return 0

    def true_neg_rate(self):
        """
        :return: float
            Calculates true negative rate on database
        """

        false_pos = self.matrix[1][0]
        true_neg = self.matrix[1][1]

        try:
            return 1.0 * true_neg / (true_neg + false_pos)
        except:  # division by 0
            return 0

    def accuracy(self):
        """
        :return: float
            Calculates accuracy on database
        """

        true_pos = self.matrix[0][0]
        false_pos = self.matrix[1][0]
        false_neg = self.matrix[0][1]
        true_neg = self.matrix[1][1]

        num = 1.0 * (true_pos + true_neg)
        den = true_pos + true_neg + false_pos + false_neg

        try:
            return num / den
        except:  # division by 0
            return 0

    def f1_score(self):
        """
        :return: float
            Calculates F1 score on database
        """

        m_pre = self.precision()
        rec = self.recall()

        try:
            return 2.0 / (1.0 / m_pre + 1.0 / rec)  # harmonic mean
        except:  # division by 0
            return 0

    def get_column(self, column_index):
        """
        :param column_index: int >= 0
            Column index to take
        :return: []
            Column of array at position given
        """

        try:
            np_matrix = np.array(self.matrix)
            np_column = np_matrix[:, column_index]
            return list(np_column)
        except:
            return []

    def get_subset(self, headers_to_sample, all_headers):
        """
        :param headers_to_sample: [] of str
            List of columns to get
        :param all_headers: [] of str
            List of all headers in matrix
        :return: [] of []
            Correlation matrix of selected columns
        """

        header_to_column = {}  # create index of headers
        for header in all_headers:
            header_to_column[header] = all_headers.index(header)

        subset_columns = []
        for header in headers_to_sample:
            header_ind = header_to_column[header]  # index of header
            header_column = self.get_column(header_ind)

            for i, value in enumerate(header_column):
                header_column[i] = float(value)  # get float

            subset_columns.append(header_column)

        return np.transpose(subset_columns)

    def remove_column(self, headers, header_to_remove):
        """
        :param headers: [] of str
            Column names
        :param header_to_remove: str
            Name of column to remove
        :return: headers, data
            Headers without header removed and data without column removed
        """

        index_to_remove = headers.index(header_to_remove)

        new_data = np.delete(self.matrix, index_to_remove, 1)  # remove
        new_headers = np.delete(headers, index_to_remove, 0)  # remove

        return new_headers, new_data

    def add_columns(self, headers, new_headers, new_columns):
        """
        :param headers: headers: [] of str
            Column names
        :param new_headers: [] of str
            Names of new columns
        :param new_columns: ([] of [])
            New columns to add
        :return: headers, data
            New headers (with new headers) and data with new columns
        """

        new_data = []  # add each column
        for i, row in enumerate(self.matrix):
            new_row = []
            for col in row:
                new_row.append(col)  # add old columns

            for new_col in new_columns[i]:
                new_row.append(new_col)  # add new columns
            new_data.append(new_row)  # add new row

        new_column_names = headers + new_headers
        return new_column_names, new_data

    def encode(self):
        """
        :return: tuple (LabelEncoder, Matrix)
            Encoder, encoded matrix
        """

        lb = LabelEncoder()  # convert
        concatenated_rows = sum([
            row
            for row in self.matrix
        ], [])  # long list of raw values
        encoded = lb.fit_transform(concatenated_rows)  # long list of encoded
        n_columns = len(self.matrix[0])
        n_rows = len(self.matrix)
        matrix = [
            encoded[i: i + n_columns]
            for i in range(0, n_rows * n_columns, n_columns)
        ]

        return lb, Matrix(matrix)

    def decode(self, lb):
        """
        :param lb: LabelEncoder
            Encoder used to encode matrix
        :return: Matrix
            Decoded matrix
        """

        return Matrix([
            lb.inverse_transform(row)
            for row in self.matrix
        ])
