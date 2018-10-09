# -*- coding: utf-8 -*-
""" Pretty prints table in SQL style """

from hal.strings.utils import non_ansi_string


def parse_colorama(text):
    """

    :param text: str
    :param Colorama: text to parse
    :returns: str
      Parsed colorama text
    """
    return non_ansi_string(text)


class SqlTable:
    def __init__(self, labels, data, num_format, line_separator):
    """

    :param labels: of str
    :param List: of labels of data
    :param data: of
    :param Matrix: of any type
    :param num_format: str
    :param Format: numbers with this format
    :param line_separator: str
    :param Separate: each new line with this
    :returns: str
          Pretty formatted table (first row is labels, then actual data)
    """
        self.labels = labels
        self.data = data
        self.num_format = num_format
        self.new_line = line_separator
        self.widths = None

        self._parse()

    def _parse(self):
        """ """
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                try:
                    x = float(col)
                    if (x % 1) == 0:  # integer
                        x = int(col)
                        self.data[i][j] = str(x)
                    else:
                        self.data[i][j] = self.num_format.format(x)
                except:
                    self.data[i][j] = str(self.data[i][j])

    def _calculate_optimal_column_widths(self):
        """:return: [] of int
            Length of longest data in each column (labels and data)

        """
        columns = len(self.data[0])  # number of columns
        str_labels = [parse_colorama(str(l)) for l in
                      self.labels]  # labels as strings
        str_data = [[parse_colorama(str(col)) for col in row] for row in
                    self.data]
        # values as strings

        widths = [0] * columns  # length of longest string in each column
        for row in str_data:  # calculate max width in each column
            widths = [max(w, len(c)) for w, c in zip(widths, row)]

        # check if label name is longer than data
        for col, label in enumerate(str_labels):
            if len(label) > widths[col]:
                widths[col] = len(label)

        self.widths = widths

    def get_pretty_row(self, row, filler, splitter):
        """
        :param row: of anything
        :param List: of data
        :param filler: char
        :param Fill: empty columns with this char
        :param splitter: char
        :param Separate: columns with this char
        :returns: str
          Pretty formatted row
        """
        for i, val in enumerate(row):
            length_diff = self.widths[i] - len(parse_colorama(val))
            if length_diff > 0:  # value is shorter than foreseen
                row[i] = str(filler * length_diff) + row[i]  # adjust content

        pretty_row = splitter  # start of row
        for val in row:
            pretty_row += filler + val + filler + splitter

        return pretty_row

    def get_blank_row(self, filler="-", splitter="+"):
        """
        :param filler: char
        :param Fill: empty columns with this char
        :param splitter: char
        :param Separate: columns with this char
        :returns: str
          Pretty formatted blank row (with no meaningful data in it)
        """
        return self.get_pretty_row(
            ["" for _ in self.widths],  # blanks
            filler,  # fill with this
            splitter,  # split columns with this
        )

    def pretty_format_row(self, row, filler=" ", splitter="|"):
        """
        :param row: of anything
        :param List: of data
        :param filler: char
        :param Fill: empty columns with this char
        :param splitter: char
        :param Separate: columns with this char
        :returns: str
          Pretty formatted row
        """
        return self.get_pretty_row(
            row,
            filler,
            splitter
        )

    def build(self):
        """ """
        self._calculate_optimal_column_widths()

        pretty_table = self.get_blank_row() + self.new_line  # first row
        pretty_table += self.pretty_format_row(self.labels) + self.new_line
        pretty_table += self.get_blank_row() + self.new_line

        for row in self.data:  # append each row
            pretty_table += self.pretty_format_row(row) + self.new_line
        pretty_table += self.get_blank_row()  # ending line

        return pretty_table

    @staticmethod
    def from_df(df):
        """
        :param df: pandas
        :param Data: 
        :returns: SqlTable
          Parses data and builds an instance of this class
        """
        labels = df.keys().tolist()
        data = df.values.tolist()
        return SqlTable(labels, data, "{:.3f}", "\n")


def pretty_format_table(labels, data, num_format="{:.3f}", line_separator="\n"):
    """

    :param labels: of str
    :param List: of labels of data
    :param data: of
    :param Matrix: of any type
    :param num_format: str
    :param Format: numbers with this format
    :param line_separator: str
    :param Separate: each new line with this
    :returns: str
      Pretty formatted table (first row is labels, then actual data)
    """
    table = SqlTable(labels, data, num_format, line_separator)
    return table.build()


def pretty_df(df):
    """

    :param df: pandas
    :param Data:
    :returns: str
      Pretty formatted table (first row is labels, then actual data)
    """
    table = SqlTable.from_df(df)
    return table.build()
