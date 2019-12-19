#!/usr/bin/env python
# coding: utf-8


def get_error(x, x_real):
    return (x - x_real).linear_norm()
