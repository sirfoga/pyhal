# -*- coding: utf-8 -*-

"""Parse anything there is on the Internet """

from bs4 import BeautifulSoup

from hal.strings.models import String


class HtmlTable:
    """Table written in HTML language"""

    def __init__(self, html_source):
        """
        :param html_source: string
            Html source of table
        """
        self.source = html_source
        self.soup = BeautifulSoup(self.source, "lxml")

    @staticmethod
    def _get_row_tag(row, tag):
        """Parses row and gets columns matching tag

        :param row: HTML row
        :param tag: tag to get
        :return: list of labels in row
        """

        is_empty = True
        data = []
        for column_label in row.find_all(tag):  # cycle through all labels
            data.append(
                String(column_label.text).strip_bad_html()
            )
            if data[-1]:
                is_empty = False

        if not is_empty:
            return data

        return None

    @staticmethod
    def _parse_row(row):
        """Parses HTML row

        :param row: HTML row
        :return: list of values in row
        """

        data = []

        labels = HtmlTable._get_row_tag(row, "th")
        if labels:
            data += labels

        columns = HtmlTable._get_row_tag(row, "td")
        if columns:
            data += columns

        return data

    def parse(self):
        """Parses data in table

        :return: List of list of values in table
        """
        data = []  # add name of section

        for row in self.soup.find_all("tr"):  # cycle through all rows
            parsed = self._parse_row(row)
            if parsed:
                data.append(parsed)

        return data


def remove_tag(tag, soup):
    [s.extract() for s in soup(tag)]
    return soup


def remove_dynamics(soup):
    dynamics_tags = ['link', 'script']

    for tag in dynamics_tags:
        soup = remove_tag(tag, soup)

    return soup


def remove_style(soup):
    return remove_tag('css', soup)
