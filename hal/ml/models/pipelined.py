#!/usr/bin/env python
# coding: utf-8


""" Prediction methods based on multiple models mixed up. """

from sklearn import linear_model
from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline


def logistic_rbm():
    """
    :return: rbm -> logistic
    """

    logistic = linear_model.LogisticRegression()
    logistic.C = 6000.0
    rbm = BernoulliRBM(random_state=0)
    rbm.learning_rate = 1
    rbm.n_iter = 10
    rbm.n_components = 10000
    clf = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)])
    return clf


def anova_svm():
    """
    :return: anova -> svc
    """

    anova_filter = SelectKBest(f_regression)
    svr = svm.SVR(kernel='poly', degree=2)  # fit a parabola
    clf = Pipeline([('anova', anova_filter), ('svc', svr)])
    clf.set_params(anova__k=20, svc__C=1e2)
    return clf
