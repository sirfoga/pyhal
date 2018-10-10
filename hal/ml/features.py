#!/usr/bin/env python
# coding: utf-8


"""Collection of methods to find weights of features and select the best
ones"""

from sklearn.feature_selection import SelectKBest, chi2, RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC


class FeatureSelect:
    """Selects best features"""

    def __init__(self, x, y):
        """
        :param x: x matrix
        :param y: y array
        """
        self.x = x
        self.y = y

    def select_k_best(self, k):
        """Selects k best features in dataset

        :param k: features to select
        :returns: k best features
        """
        x_new = SelectKBest(chi2, k=k).fit_transform(self.x, self.y)
        return x_new

    def get_best(self):
        """Finds the optimal number of features
        :returns: optimal number of features and ranking
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
