#!/usr/bin/env python
# coding: utf-8


""" Prediction methods based on regression algorithms. """

from sklearn import svm, linear_model


def support_vector_machine():
    """
    :return: sklearn svm.SVR
        Classical polynomial SVM
    """

    return svm.SVR(kernel='poly', C=1e3, degree=2)  # fit a parabola


def logistic_regression():
    """
    :return: sklearn LogisticRegression
        Logistic regression model
    """

    return linear_model.LogisticRegression(C=1e5)
