#!/usr/bin/env python
# coding: utf-8


from hal.maths.la.utils import get_error, apply_toll


def is_toll_enough(x, x_real, rel_toll, abs_toll):
    if x is None:
        return False

    if x_real is None:
        return False

    diff = get_error(x, x_real)  # todo test fix
    return diff < apply_toll(x_real, rel_toll, abs_toll)
