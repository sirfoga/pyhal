# !/usr/bin/python3
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
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

""" Pretty prints table in SQL style """


def get_optimal_column_widths(labels, data):
    """
    :param labels: [] of str
        List of labels of data
    :param data: ([] of []) of anything
        Matrix of any type
    :return: [] of int
        Length of longest data in each column (labels and data)
    """

    columns = len(data[0])  # number of columns
    str_labels = [str(l) for l in labels]  # labels as strings
    str_data = [[str(col) for col in row] for row in data]  # values as strings

    widths = [0] * columns  # length of longest string in each column
    for row in str_data:  # calculate max width in each column
        widths = [max(w, len(c)) for w, c in zip(widths, row)]

    # check if label name is longer than data
    for col, label in enumerate(str_labels):
        if len(label) > widths[col]:
            widths[col] = len(label)

    return widths


def get_pretty_row(data, widths, filler, splitter):
    """
    :param data: [] of anything
        List of data
    :param widths: [] of int
        Length of longest data in each column
    :param filler: char
        Fill empty columns with this char
    :param splitter: char
        Separate columns with this char
    :return: str
        Pretty formatted row
    """

    row = [str(d) for d in data]
    for i, val in enumerate(row):
        length_diff = widths[i] - len(val)
        if length_diff > 0:  # value is shorter than forseen
            row[i] = str(filler * length_diff) + row[i]  # adjust content
    pretty_row = splitter  # start of row
    for val in row:
        pretty_row += filler + val + filler + splitter
    return pretty_row


def get_blank_row(widths, filler="-", splitter="+"):
    """
    :param widths: [] of int
        Length of longest data in each column
    :param filler: char
        Fill empty columns with this char
    :param splitter: char
        Separate columns with this char
    :return: str
        Pretty formatted blank row (with no meaningful data in it)
    """

    return get_pretty_row(
        ["" for _ in widths],  # blanks
        widths,  # same columns widths
        filler,  # fill with this
        splitter,  # split columns with this
    )


def pretty_format_row(data, widths, filler=" ", splitter="|"):
    """
    :param data: [] of anything
        List of data
    :param widths: [] of int
        Length of longest data in each column
    :param filler: char
        Fill empty columns with this char
    :param splitter: char
        Separate columns with this char
    :return: str
        Pretty formatted row
    """

    return get_pretty_row(
        data,
        widths,
        filler,
        splitter
    )


def pretty_format_table(labels, data, line_separator="\n"):
    """
    :param labels: [] of str
        List of labels of data
    :param data: ([] of []) of anything
        Matrix of any type
    :param line_separator: str
        Separate each new line with this
    :return: str
        Pretty formatted table (first row is labels, then actual data)
    """

    widths = get_optimal_column_widths(labels, data)
    pretty_table = get_blank_row(widths) + line_separator  # first row
    pretty_table += pretty_format_row(labels, widths) + line_separator
    pretty_table += get_blank_row(widths) + line_separator
    for row in data:  # append each row
        pretty_table += pretty_format_row(row, widths) + line_separator
    pretty_table += get_blank_row(widths)  # ending line
    return pretty_table