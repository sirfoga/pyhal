#!/usr/bin/env python
# coding: utf-8

from collections import namedtuple

from hal.lists.utils import lst2str
from hal.maths.combo.utils import get_superset

MachineNumber = namedtuple('MachineNumber', ['sign', 'mantissa', 'exponent'])


# Returns a list of strings. Each one of them is a mantissa.
def get_all_possible_mantissa(b, l):
    digits = range(b)  # all possible digits with such base
    mantissas = get_superset(digits, l - 1)  # first l - 1 digits

    full_mantissas = []
    for digit in digits:
        if digit > 0:  # mantissa has to start with a positive number
            def add_first_digit(x):
                return (digit, *x)  # unpack tuple

            mantissa_starting_with_that_digit = map(add_first_digit, mantissas)
            full_mantissas += mantissa_starting_with_that_digit

    zero_mantissa = tuple([0 for _ in range(l)])
    full_mantissas.append(zero_mantissa)

    def mantissa2string(x):
        return ''.join(map(str, x))

    return map(mantissa2string, full_mantissas)


# Returns a list of strings. Each one of them is a exponent.
def get_all_possible_exponents(b, k):
    digits = range(b)  # all possible digits with such base
    absolutes = get_superset(digits, k)
    positives = list(map(lst2str, absolutes))
    negatives = map(lambda x: '-' + x, positives)
    return positives + list(negatives)


def get_all_machine_numbers(b, l, k):
    all_mantissas = get_all_possible_mantissa(b, l)
    all_exponents = get_all_possible_exponents(b, k)
    return [
        MachineNumber(sign, mantissa, exponent)
        for mantissa in all_mantissas
        for exponent in all_exponents
        for sign in ['+', '-']
    ]


def convert_machine_numbers(numbers, in_base):
    def convert(number):
        def convert_mantissa(mantissa, in_base):
            return sum(
                float(digit) * ((1 / in_base) ** (i + 1))
                for i, digit in enumerate(mantissa)
            )

        new_mantissa = convert_mantissa(number.mantissa, in_base)  # 2 decimal
        new_exponent = float(int(number.exponent, in_base))
        raw = number.sign + str(new_mantissa * in_base ** new_exponent)
        return float(raw)

    return map(convert, numbers)
