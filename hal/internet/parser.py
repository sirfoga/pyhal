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


""" Parse anything there is on the Internet. """


from bs4 import BeautifulSoup


class HtmlTable(object):
    def __init__(self, html_source):
        """
        :param html_source: string
            Html source of table
        """

        object.__init__(self)

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
                    strip_raw_html_string(column_label.text)
                )

            for column in row.find_all("td"):  # cycle through all columns
                data_row.append(
                    strip_raw_html_string(column.text)
                )

            data.append(data_row)
        return data


def strip_raw_html_string(string):
    """
    :param string: string
        String to parse
    :return: string
        Given string with raw HTML elements removed
    """

    out = string.replace("\n", "") \
        .replace("\r", "") \
        .replace("\t", "") \
        .strip()

    while out.find("  ") > 0:  # while there are multiple blanks in a row
        out = out.replace("  ", " ")
    return out.encode("utf-8")
