# -*- coding: utf-8 -*-

"""Matrix computations"""

from numpy import array
from numpy.linalg import eigvalsh


def eigenvalues_hadamard(a, b):
    """Computes the Hadamard product of 2 matrices. See
    https://www.johndcook.com/blog/2018/10/10/hadamard-product/ for details.

    :param a: first matrix
    :param b: second matrix
    :return: lower and upper
    """

    a = array(a)  # as arrays
    b = array(b)

    eig_a = eigvalsh(a)  # eigenvalues (optimized for Hermitian matrices)
    eig_b = eigvalsh(b)

    return eig_a, eig_b
