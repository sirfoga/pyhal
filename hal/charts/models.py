# !/usr/bin/python3
# coding: utf-8


""" Chart model """

from matplotlib import pyplot as plt


class SimpleChart:
    """Simple matplotlib chart"""

    def __init__(self, title, grid=True):
        """
        Setups bottom margin

        # Attributes
            title: Title of chart
            fig: Matplotlib figure
        """
        self.title = title
        self.fig = plt.figure()
        plt.title(title)
        plt.grid(grid)

    def setup(self, bottom):
        """
        Setups bottom margin

        # Arguments
            bottom: Bottom margin
        """
        plt.gcf().subplots_adjust(bottom=bottom)  # add bottom

    def get_fig(self):
        """
        Gets chart canvas

        # Returns
            figure: matplotlib figure
        """
        return self.fig

    def create(self):
        """
        Adds to figure

        # Returns
            completed: operation completed
        """
        return self.fig.add_subplot(111)
