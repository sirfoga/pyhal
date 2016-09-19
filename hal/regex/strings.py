# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" STRINGS: manipulate and edit strings """


import re
from enum import Enum


class Color(Enum):
    """ basic color to output formatted text in shell """

    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    def __add__(self, other):
        return self + other


def occur(string, pattern, casesensitive=True):
    """
    :param string: long string to find occurrences of..
    :param pattern: patter
    :param casesensitive: if case is sensitive
    :return: find numb of occurrences of pattern in substring
    """

    if not casesensitive:
        string = string.lower()
        pattern = string.lower()
    l = len(pattern)
    ct = 0
    for c in range(0, len(string)):
        if string[c:c+l] == pattern:
            ct += 1
    return ct


def only_letters(name):
    """
    :param name: name to be edited
    :return: returns given string without numbers
    """

    result = name.replace('à', 'a')
    result = result.replace('è', 'e')
    result = result.replace('ì', 'i')
    result = result.replace('ò', 'o')
    result = result.replace('ù', 'u')
    result = re.sub('^[^a-zA-z]*|[^a-zA-Z]*$', '', result)

    # adjust parenthesis
    if result.count('(') != result.count(')'):
        result += ')'

    return result


def string2digit(literal):
    """
    :param string: number in italian language
    :return: string converted to int
    """
    
    literal = literal.lower()
    literals = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']

    return literals.index(literal)
