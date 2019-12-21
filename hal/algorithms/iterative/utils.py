#!/usr/bin/env python
# coding: utf-8


from maths.la.utils import get_error


def is_toll_enough(x, x_real, abs_toll, rel_toll):
    if x is None:
        return False

    if x_real is None:
        return False

    diff = get_error(x, x_real)
    return diff < (x_real * rel_toll).linear_norm() + abs_toll
