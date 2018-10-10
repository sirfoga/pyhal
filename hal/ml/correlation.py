# -*- coding: utf-8 -*-

"""Correlate values in arrays producing fancy good-looking matrices"""

import os
import time

import numpy as np
from matplotlib import pyplot

from hal.charts import correlation as cr_plot
from hal.data.matrix import Matrix
from hal.files.models.files import Document
from hal.files.models.system import list_content
from hal.files.parsers import CSVParser


class CorrelationMatrix:
    def __init__(self, title, headers_to_test, headers, data):
        """

        :param title: Title to show
        :param headers_to_test: List of columns to get correlation matrix of
        :param headers: List of all headers in matrix
        :param data: Matri: of float values
        """
        self.title = title
        self.headers_to_test = headers_to_test
        self.headers = headers
        self.data = data

    @staticmethod
    def get_correlation_matrix(matrix):
        """Finds correlation matrix of matrix

        :param matrix: List of features to get correlation matrix
        :returns: correlation matrix
        """
        return np.corrcoef(matrix)

    def show_correlation_matrix(self, correlation_matrix):
        """Shows the given correlation matrix as image

        :param correlation_matrix: Correlation matrix of features
        """
        cr_plot.create_correlation_matrix_plot(
            correlation_matrix, self.title, self.headers_to_test
        )
        pyplot.show()

    def show_correlation_matrix_of_columns(self):
        """Shows the correlation matrix of columns"""
        correlation_matrix = self.get_correlation_matrix_of_columns()
        self.show_correlation_matrix(correlation_matrix)

    def get_correlation_matrix_of_columns(self):
        """Computes correlation matrix of columns
        :returns: Correlation matrix of columns
        """
        header_to_column = {}  # create index of headers
        for header in self.headers:
            header_to_column[header] = self.headers.index(header)

        data_to_test = []
        for header in self.headers_to_test:
            header_column = Matrix(self.data) \
                .get_column(header_to_column[header])

            for i, value in enumerate(header_column):
                header_column[i] = float(value)  # get float

            data_to_test.append(header_column)

        return self.get_correlation_matrix(data_to_test)

    def save_to_file(self, out_file):
        """Saves correlation matrix of selected headers

        :param out_file: Output file
        """
        correlation_matrix = self.get_correlation_matrix_of_columns()
        cr_plot.create_correlation_matrix_plot(
            correlation_matrix, self.title, self.headers_to_test)

        fig = pyplot.gcf()  # get reference to figure
        fig.set_size_inches(23.4, 23.4)
        pyplot.savefig(out_file, dpi=120)

    @staticmethod
    def save_correlation_matrix_of_data_files_in_folder(folder_path):
        """Saves each file's correlation matrix of common headers

        :param folder_path: Folder containing logs data
        """
        file_name = "output-" + str(int(time.time()))
        output_folder = os.path.join(folder_path, file_name)
        os.makedirs(output_folder)  # make necessary folders to create directory

        for file in list_content(folder_path, False, False):
            if os.path.isfile(file) and str(file).endswith("csv"):
                print("Analysing file ", str(file))

                file_name = Document(file).name.strip()
                output_file_name = file_name + ".png"  # save output as image
                output_file_path = os.path.join(output_folder, output_file_name)
                headers, data = CSVParser.get_headers_data(file)  # parse
                matrix = CorrelationMatrix(
                    "Correlation of logs data for file " + file_name,
                    headers,
                    headers,
                    data
                )
                matrix.save_to_file(output_file_path)
