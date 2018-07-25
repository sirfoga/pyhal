# !/usr/bin/python3
# coding: utf-8


""" Parse anything there is on the Internet. """

from bs4 import BeautifulSoup


class HtmlTable(str):
    """ Table written in HTML language """

    def __init__(self, html_source):
        """
        :param html_source: string
            Html source of table
        """

        str.__init__(html_source)
        self.source = html_source
        self.soup = BeautifulSoup(html_source)

    def parse(self):
        """
        :return: list of list
            List of list of values in table
        """

        data = []  # add name of section
        for row in self.soup.find_all("tr"):  # cycle through all rows
            data_row = []
            for column_label in row.find_all("th"):  # cycle through all labels
                data_row.append(
                    html_stripper(column_label.text)
                )

            for column in row.find_all("td"):  # cycle through all columns
                data_row.append(
                    html_stripper(column.text)
                )

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
