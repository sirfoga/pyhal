# !/usr/bin/python3
# coding: utf-8

""" Correlate values in arrays producing fancy good-looking matrices """

import os

import numpy as np
from matplotlib import pyplot

from data.matrix import get_column_of_matrix
from hal.charts import correlation as cr_plot
from hal.files.models.files import Document
from hal.files.models.system import list_content
from hal.files.parsers import CSVParser
from times import time


class CorrelationMatrix:
    def __init__(self, title, headers_to_test, headers, data):
        """
        :param title: str
            Title to show
        :param headers_to_test: [] of str
            List of columns to get correlation matrix of
        :param headers: [] of str
            List of all headers in matrix
        :param data: [] of []
            Matrix of float values
        """

        self.title = title
        self.headers_to_test = headers_to_test
        self.headers = headers
        self.data = data

    @staticmethod
    def get_correlation_matrix(matrix):
        """
        :param matrix: [] of []
            List of features to get correlation matrix
        :return: [] of []
            correlation matrix
        """

        return np.corrcoef(matrix)

    def show_correlation_matrix(self, correlation_matrix):
        """
        :param correlation_matrix: [] of []
            Correlation matrix of features
        :return: void
            shows the given correlation matrix as image
        """

        cr_plot.create_correlation_matrix_plot(
            correlation_matrix, self.title, self.headers_to_test
        )
        pyplot.show()

    def show_correlation_matrix_of_columns(self):
        correlation_matrix = self.get_correlation_matrix_of_columns()
        self.show_correlation_matrix(correlation_matrix)

    def get_correlation_matrix_of_columns(self):
        """
        :return: [] of []
            Correlation matrix of selected columns
        """

        header_to_column = {}  # create index of headers
        for header in self.headers:
            header_to_column[header] = self.headers.index(header)

        data_to_test = []
        for header in self.headers_to_test:
            header_column = get_column_of_matrix(
                header_to_column[header], self.data
            )

            for i, value in enumerate(header_column):
                header_column[i] = float(value)  # get float

            data_to_test.append(header_column)

        return get_correlation_matrix(data_to_test)

    def save_to_file(self, out_file):
        """
        :param out_file: str
            Output file
        :return: void
            Saves correlation matrix of selected headers
        """

        correlation_matrix = self.get_correlation_matrix_of_columns()
        cr_plot.create_correlation_matrix_plot(
            correlation_matrix, self.title, self.headers_to_test)

        fig = pyplot.gcf()  # get reference to figure
        fig.set_size_inches(23.4, 23.4)
        pyplot.savefig(out_file, dpi=120)

    @staticmethod
    def save_correlation_matrix_of_data_files_in_folder(folder_path):
        """
        :param folder_path: str
            Folder containing logs data
        :return: void
            Saves each file's correlation matrix of common headers
        """

        output_folder = os.path.join(folder_path, "output-" + str(int(time())))
        os.makedirs(output_folder)  # make necessary folders to create directory

        for file in list_content(folder_path, False, False):
            if os.path.isfile(file) and str(file).endswith("csv"):
                print("Analysing file ", str(file))

                file_name = Document(file).name.strip()
                output_file_name = file_name + ".png"  # save output as image
                output_file_path = os.path.join(output_folder, output_file_name)

                try:
                    headers, data = CSVParser.get_headers_data(file)  # parse
                    matrix = CorrelationMatrix(
                        "Correlation of logs data for file " + file_name,
                        headers,
                        headers,
                        data
                    )
                    matrix.save_to_file(output_file_path)
                except:
                    print("Cannot save correlation matrix of file \"",
                          str(file),
                          "\"")
