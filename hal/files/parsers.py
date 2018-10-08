#!/usr/bin/env python
# coding: utf-8


""" Parsers for raw databases """

import csv


class Parser:
    """Mother of all data-files parsers"""

    def __init__(self, file_path):
        """
        # Arguments
            file_path: a raw .csv file that contains any data
            about anything
        """
        self.path = file_path
        self.lines = None  # list of lines in database

    def get_lines(self):
        """
        Gets lines in file

        # Returns:
            lines: Lines in file
        """
        with open(self.path) as data:
            self.lines = data.readlines()  # store data in arrays

        return self.lines


class CSVParser(Parser):
    """Parses CSV data files"""

    def __init__(self, file_path, encoding="utf-8"):
        """
        # Arguments
            file_path: a raw .csv file that contains any data
            about anything
            encoding: str
            Encoding to open file with
        """
        super().__init__(file_path)
        self.encoding = str(encoding).strip()

    def get_matrix(self):
        """
        Stores values in array, store lines in array.

        # Returns:
            data: 2D matrix
        """
        data = []
        with open(self.path, encoding=self.encoding) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",", quotechar="\"")
            for row in csv_reader:
                data.append(row)

        return data

    def get_headers_data(self):
        """
        Gets headers and data

        # Returns:
            headers: headers of file
            data: data of file
        """
        data = self.get_matrix()
        return data[0], data[1:]  # headers, data

    def get_dicts(self):
        """
        Gets dicts in file

        # Returns:
            generator; List of dicts with data from .csv file
        """
        reader = csv.DictReader(open(self.path, "r", encoding=self.encoding))
        for row in reader:
            if row:
                yield row
