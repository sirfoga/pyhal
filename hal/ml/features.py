#!/usr/bin/env python
# coding: utf-8


""" Collection of methods to find weights of features and select the best
ones. """

from sklearn.feature_selection import SelectKBest, chi2, RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC


def select_k_best(x_data, y_data, num_features):
    """ select k best features in dataset """

    x_new = SelectKBest(chi2, k=num_features).fit_transform(x_data, y_data)
    return x_new


def get_best_features(x_data, y_data):
    """ finds the optimal number of features """

    svc = SVC(kernel="linear")
    rfecv = RFECV(
        estimator=svc,
        step=1,
        cv=StratifiedKFold(y_data, 2),
        scoring="log_loss"
    )
    rfecv.fit(x_data, y_data)
    return rfecv.n_features_, rfecv.ranking_
