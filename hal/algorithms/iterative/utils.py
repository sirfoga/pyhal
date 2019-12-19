#!/usr/bin/env python
# coding: utf-8


def is_enough_toll(x, x_real, abs_toll, rel_toll):
    if x is None:
        return False

    if x_real is None:
        return False

    diff = utils.get_error(x, x_real)
    return diff < (x_real * rel_toll).linear_norm() + abs_toll
