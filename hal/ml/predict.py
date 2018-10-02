#!/usr/bin/env python
# coding: utf-8


"""" General model to make prediction about everything """

from sklearn.model_selection import train_test_split


class BasePrediction(object):
    """ The mother of all predictions """

    def __init__(self, model, rounds):
        """
        :param model: sklearn.model
            Model chosen for prediction
        :param rounds: int
            Number of rounds to repeat prediction (and get better results)
        """

        object.__init__(self)

        self.model = model  # ml algorithm to use for prediction
        self.rounds = rounds  # number of times to make prediction

    def train(self, x_data, y_data):
        """
        :param x_data: data
            Input x
        :param y_data: data
            Input y
        :return: void
            Train model on inputs
        """

        x_train, _, y_train, _ = train_test_split(
            x_data,
            y_data,
            test_size=0.67,
            random_state=None
        )  # cross-split

        self.model.fit(x_train, y_train)  # fit model
