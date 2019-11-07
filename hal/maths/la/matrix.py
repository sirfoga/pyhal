#!/usr/bin/env python
# coding: utf-8

import numpy as np

from hal.lists.utils import lst2str


class BaseMatrix:
    def __init__(self, matrix):
        self.m = np.matrix(matrix)

    def __add__(self, other):
        if isinstance(other, BaseMatrix):
            other = other.m

        return Matrix(np.add(self.m, other))

    def __radd__(self, other):
        return other.__add__(self)

    def __sub__(self, other):
        if isinstance(other, BaseMatrix):
            other = other.m

        return Matrix(np.subtract(self.m, other))

    def __rsub__(self, other):
        return other.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, BaseMatrix):
            other = other.m

        return Matrix(np.dot(self.m, other))

    def __rmul__(self, other):
        return other.__mul__(self)

    def to_numpy(self):
        return self.m


class Matrix(BaseMatrix):
    def __init__(self, matrix):
        super().__init__(matrix)

    def shape(self):
        return self.m.shape

    def get_n_rows(self):
        return self.shape()[0]

    def get_n_cols(self):
        return self.shape()[1]

    def get_rows(self):
        return [
            [row.tolist()[0] for row in self.m]
        ][0]

    def get_cols(self):
        return [
            [col.tolist()[0] for col in self.m.T]
        ][0]

    def get_at(self, row, col):
        return self.m[row, col]

    def is_square(self):
        rows, cols = self.shape()
        return rows == cols

    def transpose(self):
        return Matrix(self.m.T)

    def inverse(self):
        return Matrix(np.linalg.inv(self.m))

    def is_symmetric(self):
        return self == self.transpose()

    def is_diagonally_dominant(self, strictly=False):
        for i, row in enumerate(self.m):
            diagonal_element = row[0, i]
            sum_of_others = np.sum(row) - diagonal_element

            if abs(diagonal_element) < sum_of_others:
                return False

            if abs(diagonal_element) <= sum_of_others and strictly:
                return False
        return True

    def check_on(self, f):
        for row in range(self.get_n_rows()):
            for col in range(self.get_n_cols()):
                element = self.get_at(row, col)
                if not f(element):
                    return False
        return True

    def is_definite_positive(self):
        def is_positive(x):
            return x > 0

        return self.check_on(is_positive)

    def eigens(self):
        values, vectors = np.linalg.eig(self.m)
        return values.tolist(), vectors.tolist()

    def spectral_radius(self):
        eigenvalues, _ = self.eigens()
        spectral_radius = max(map(abs, eigenvalues))
        return spectral_radius

    def get_diagonal(self):
        D = np.zeros(self.shape())
        for i, row in enumerate(self.m):
            D[i, i] = row[0, i]  # diagonal element
        return Matrix(D)

    def get_lower(self):
        L = np.zeros(self.shape())
        for i, row in enumerate(self.m):
            for j in range(i):  # without the diagonal
                L[i, j] = row[0, j]
        return Matrix(L)

    def get_upper(self):
        U = np.zeros(self.shape())
        for i, row in enumerate(self.m):
            for j in range(i + 1, self.shape()[0]):  # without the diagonal
                U[i, j] = row[0, j]
        return Matrix(U)

    def linear_norm(self):
        """ Works only if vector """

        return np.linalg.norm(self.m)

    def l1_norm(self):
        abs_cols = [
            list(map(abs, col)) for col in self.get_cols()
        ]
        sums = [
            np.sum(col) for col in abs_cols
        ]
        return max(sums)

    def l2_norm(self):
        tmp = self * self.transpose()
        eigenvalues, _ = tmp.eigens()
        return np.sqrt(np.max(eigenvalues))

    def linfinite_norm(self):
        abs_rows = [
            list(map(abs, row)) for row in self.get_rows()
        ]
        sums = [
            np.sum(row) for row in abs_rows
        ]
        return max(sums)

    def condition_number(self):
        inv = np.linalg.inv(self.m)
        return self.l2_norm() * inv.l2_norm()

    def eigenvalues_hadamard(self, other):
        """Computes the Hadamard product of 2 matrices. See
        https://www.johndcook.com/blog/2018/10/10/hadamard-product/ for details

        :param other: second matrix
        :return: lower and upper
        """

        if isinstance(other, Matrix):
            other = other.to_numpy()

        eig_a = np.linalg.eigvalsh(self.to_numpy())  # eigenvalues (optimized for Hermitian matrices)
        eig_b = np.linalg.eigvalsh(other)

        return eig_a, eig_b

    def __eq__(self, other):
        if isinstance(other, list):
            other = Matrix(other)

        if self.shape() != other.shape():
            return False

        for row in range(self.get_n_rows()):
            for col in range(self.get_n_cols()):
                if self.get_at(row, col) != other.get_at(row, col):
                    return False

        return True

    def __str__(self):
        out = ''
        for row in self.get_rows():
            out += '| ' + lst2str(row, ' | ') + ' |'
            out += '\n'
        return out


class LinearSystemMatrix(Matrix):
    def incomplete_Cholesky(self):
        pass  # todo

    def does_jacobi_converge(self):
        return self.is_diagonally_dominant(strictly=True)

    def does_gauss_seidel_converge(self):
        return self.is_diagonally_dominant(strictly=True) or self.is_definite_positive()

    def dlu_decompose(self):
        return self.get_diagonal(), self.get_lower(), self.get_upper()
