#!/usr/bin/env python
# coding: utf-8


"""General model to make prediction about everything"""

from sklearn.model_selection import train_test_split


class BasePrediction:
    """The mother of all predictions"""

    def __init__(self, model, rounds):
        """
        :param model: Model chosen for prediction
        :param rounds: Number of rounds to repeat prediction
        """
        self.model = model  # ml algorithm to use for prediction
        self.rounds = rounds  # number of times to make prediction

    def train(self, x_data, y_data):
        """Trains model on inputs

        :param x_data: x matrix
        :param y_data: y array
        """
        x_train, _, y_train, _ = train_test_split(
            x_data,
            y_data,
            test_size=0.67,
            random_state=None
        )  # cross-split

        self.model.fit(x_train, y_train)  # fit model
