# !/usr/bin/python3
# coding: utf-8


""" Parse anything there is on the Internet """

from bs4 import BeautifulSoup


class HtmlTable:
    """ Table written in HTML language """

    def __init__(self, html_source):
        """
        :param html_source: string
            Html source of table
        """

        self.source = html_source
        self.soup = BeautifulSoup(self.source, "lxml")

    def parse(self):
        """
        :return: list of list
            List of list of values in table
        """

        data = []  # add name of section
        for row in self.soup.find_all("tr"):  # cycle through all rows
            is_empty = True
            data_row = []

            for column_label in row.find_all("th"):  # cycle through all labels
                data_row.append(
                    html_stripper(column_label.text)
                )
                if len(data_row[-1]) > 0:
                    is_empty = False

            for column in row.find_all("td"):  # cycle through all columns
                data_row.append(
                    html_stripper(column.text)
                )
                if len(data_row[-1]) > 0:
                    is_empty = False

            if not is_empty:
                data.append(data_row)
        return data


def is_string_well_formatted(string):
    """
    :param string: string
        String to parse
    :return: bool
        True iff string is good formatted
    """

    # False iff there are at least \n, \r, \t,"  "
    is_bad_formatted = ":" in string or \
                       "\\'" in string or \
                       "\n" in string or \
                       "\r" in string or \
                       "\t" in string or \
                       "\\n" in string or \
                       "\\r" in string or \
                       "\\t" in string or \
                       "  " in string
    return not is_bad_formatted


def html_stripper(string):
    """
    :param string: string
        String to parse
    :return: string
        Given string with raw HTML elements removed
    """

    out = string
    while not is_string_well_formatted(
            out):  # while there are some improvements to do
        out = out.replace(":", "") \
            .replace("\\'", "\'") \
            .replace("\\n", "") \
            .replace("\\r", "") \
            .replace("\\t", "") \
            .replace("\n", "") \
            .replace("\r", "") \
            .replace("\t", "") \
            .replace("  ", " ") \
            .strip()

    return str(out)
