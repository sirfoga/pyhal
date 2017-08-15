#!/usr/bin/env python
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
