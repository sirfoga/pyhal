#!/usr/bin/env python
# coding: utf-8

"""Functions to deal with matrices"""

from sklearn.preprocessing import LabelEncoder

from hal.maths.utils import divide


class Matrix:
    """Table of data"""

    def __init__(self, matrix):
        self.matrix = matrix

    def precision(self):
        """Calculates precision
        
        :returns: Precision of matrix
        """
        true_pos = self.matrix[0][0]
        false_pos = self.matrix[1][0]
        return divide(1.0 * true_pos, true_pos + false_pos)

    def recall(self):
        """Calculates recall
        
        :returns: Recall
        """
        true_pos = self.matrix[0][0]
        false_neg = self.matrix[0][1]
        return divide(1.0 * true_pos, true_pos + false_neg)

    def true_neg_rate(self):
        """Calculates true negative rate
        
        :returns: true negative rate
        """
        false_pos = self.matrix[1][0]
        true_neg = self.matrix[1][1]
        return divide(1.0 * true_neg, true_neg + false_pos)

    def accuracy(self):
        """Calculates accuracy
        
        :returns: Accuracy
        """
        true_pos = self.matrix[0][0]
        false_pos = self.matrix[1][0]
        false_neg = self.matrix[0][1]
        true_neg = self.matrix[1][1]

        num = 1.0 * (true_pos + true_neg)
        den = true_pos + true_neg + false_pos + false_neg

        return divide(num, den)

    def f1_score(self):
        """Calculates F1 score
        
        :returns: F1 score
        """
        m_pre = self.precision()
        rec = self.recall()
        return divide(2.0, 1.0 / m_pre + 1.0 / rec)  # harmonic mean

    def get_as_list(self):
        """List of all values in matrix
        
        :returns: list representation
        """
        return sum([
            row
            for row in self.matrix
        ], [])

    def encode(self):
        """Encodes matrix
        
        :returns: Encoder used
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
        """Decodes matrix

        :param lb: Encoder used to encode matrix
        :returns: list: Decodes matrix
        """
        self.matrix = [
            lb.inverse_transform(row)
            for row in self.matrix
        ]

    def get_column(self, index):
        """Gets column at given index

        :param index: index of column
        :returns: Column
        """

        return [
            row[index]
            for row in self.matrix
        ]

    @staticmethod
    def from_columns(columns):
        """Parses raw columns

        :param columns: matrix divided into columns
        :returns: Matrix: Merge the columns to form a matrix
        """
        data = [
            [
                column[i]
                for i in range(len(column))
            ]
            for column in columns
        ]
        return Matrix(data)
