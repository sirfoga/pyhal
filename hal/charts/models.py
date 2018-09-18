# !/usr/bin/python3
# coding: utf-8


""" Chart model """

from matplotlib import pyplot as plt


class SimpleChart:
    """ Simple matplotlib chart """

    def __init__(self, title, grid=True):
        """
        :param title: str
            Title of chart
        :param grid: bool
            True iff you want a chart with the grid
        """

        self.title = title
        self.fig = plt.figure()
        plt.title(title)
        plt.grid(grid)

    def setup(self, bottom):
        """
        :param bottom: float
            Bottom margin
        :return: void
            Setups bottom margin
        """

        plt.gcf().subplots_adjust(bottom=bottom)  # add bottom

    def get_fig(self):
        """
        :return: matplotlib figure
            Chart canvas
        """

        return self.fig

    def create(self):
        return self.fig.add_subplot(111)
