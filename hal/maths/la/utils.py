#!/usr/bin/env python
# coding: utf-8


def modulus(x):
    try:
        return x.linear_norm()
    except:
        return abs(x)


def get_error(x, x_real):
    diff = x - x_real
    return modulus(diff)


def apply_toll(x, rel_toll, abs_toll):
    x *= rel_toll
    x = modulus(x)
    x += abs_toll
    return x
