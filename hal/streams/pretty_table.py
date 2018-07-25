# !/usr/bin/python3
# coding: utf-8

""" Pretty prints table in SQL style """

from pyparsing import Literal, Word, nums, Combine, Optional, delimitedList, \
    alphas, oneOf, Suppress


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
    str_labels = [parse_colorama(str(l)) for l in labels]  # labels as strings
    str_data = [[parse_colorama(str(col)) for col in row] for row in data]
    # values as strings

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
        length_diff = widths[i] - len(parse_colorama(val))
        if length_diff > 0:  # value is shorter than foreseen
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


def parse_colorama(text):
    """
    :param text: str
        Colorama text to parse
    :return: str
        Parsed colorama text
    """

    esc_key = Literal('\x1b')
    integer = Word(nums)
    escape_seq = Combine(
        esc_key + '[' + Optional(delimitedList(integer, ';')) +
        oneOf(list(alphas)))
    non_ansi_string = lambda s: Suppress(escape_seq).transformString(s)
    return non_ansi_string(text)
