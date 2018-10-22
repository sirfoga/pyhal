# -*- coding: utf-8 -*-

"""Matrix computations"""

from numpy import array
from numpy.linalg import eigvalsh


def eigenvalues_hadamard(matrix1, matrix2):
    """Computes the Hadamard product of 2 matrices. See
    https://www.johndcook.com/blog/2018/10/10/hadamard-product/ for details

    :param matrix1: first matrix
    :param matrix2: second matrix
    :return: lower and upper
    """

    matrix1 = array(matrix1)  # as arrays
    matrix2 = array(matrix2)

    eig_a = eigvalsh(matrix1)  # eigenvalues (optimized for Hermitian matrices)
    eig_b = eigvalsh(matrix2)

    return eig_a, eig_b
