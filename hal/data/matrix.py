#!/usr/bin/env python
# coding: utf-8

""" Functions to deal with matrices """

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

    def get_as_list(self):
        """
        :return: [] of anything
            List of all values in matrix
        """

        return sum([
            row
            for row in self.matrix
        ], [])

    def get_column(self, index):
        """
        :param index: int >= 0
            Column index to take
        :return: []
            Column of array at position given
        """

        return [
            row[index]
            for row in self.matrix
        ]

    def get_columns(self, indices):
        """
        :param indices: [] of int
            List of all index to get
        :return: [] of []
            Selected columns
        """

        return [
            [
                row[index]
                for index in indices
            ]
            for row in self.matrix
        ]

    def add_column(self, column):
        """
        :param column: [] of anything
            New column to add
        :return: void
            Data with new column
        """

        self.matrix = [
            row + [column[i]]
            for i, row in enumerate(self.matrix)
        ]

    def add_columns(self, columns):
        """
        :param columns: [] of [] of anything
            New columns to add
        :return: void
            Data with new columns
        """

        for column in columns:
            self.add_column(column)

    def remove_column(self, index):
        """
        :param index: int
            Index of column to remove
        :return: void
            Matrix without column removed
        """

        self.matrix = [
            [
                val
                for i, val in enumerate(row)
                if i != index
            ]
            for row in self.matrix
        ]

    def remove_columns(self, indices):
        """
        :param indices: [] of int
            Indices of columns to remove
        :return: void
            Matrix without column removed
        """

        for index in sorted(indices, reverse=True):  # start from last column
            self.remove_column(index)

    def encode(self):
        """
        :return: LabelEncoder
            Encoder
        """

        lb = LabelEncoder()  # encoder
        values = self.get_as_list()
        encoded = lb.fit_transform(values)  # long list of encoded
        n_columns = len(self.matrix[0])
        n_rows = len(self.matrix)

        self.matrix = [
            encoded[i: i + n_columns]
            for i in range(0, n_rows * n_columns, n_columns)
        ]

        return lb

    def decode(self, lb):
        """
        :param lb: LabelEncoder
            Encoder used to encode matrix
        :return: void
            Decodes matrix
        """

        self.matrix = [
            lb.inverse_transform(row)
            for row in self.matrix
        ]
