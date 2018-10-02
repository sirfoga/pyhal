#!/usr/bin/env python
# coding: utf-8


""" Collection of methods to find weights of features and select the best
ones """

from sklearn.feature_selection import SelectKBest, chi2, RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC


class FeatureSelect:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def select_k_best(self, k):
        """
        :param k: int
            K features to select
        :return: matrix
            Select k best features in dataset
        """

        x_new = SelectKBest(chi2, k=k).fit_transform(self.x, self.y)
        return x_new

    def get_best(self):
        """
        :return: tuple
            Finds the optimal number of features
        """

        svc = SVC(kernel="linear")
        rfecv = RFECV(
            estimator=svc,
            step=1,
            cv=StratifiedKFold(self.y, 2),
            scoring="log_loss"
        )
        rfecv.fit(self.x, self.y)
        return rfecv.n_features_, rfecv.ranking_
