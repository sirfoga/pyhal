# !/usr/bin/python3
# coding: utf-8


""" Chart model """

from matplotlib import pyplot as plt


class SimpleChart:
    """Simple matplotlib chart"""

    def __init__(self, title, grid=True):
        """
        Setups bottom margin

        Args:
          title: Title of chart
          grid: True iff you want a chart with the grid
        """
        self.title = title
        self.fig = plt.figure()
        plt.title(title)
        plt.grid(grid)

    def setup(self, bottom):
        """
        Setups bottom margin

        Args:
          bottom: Bottom margin
        """
        plt.gcf().subplots_adjust(bottom=bottom)  # add bottom

    def get_fig(self):
        """
        Gets chart canvas

        Returns: matplotlib figure
        """
        return self.fig

    def create(self):
        """
        Adds to figure

        Returns: operation completed
        """
        return self.fig.add_subplot(111)
