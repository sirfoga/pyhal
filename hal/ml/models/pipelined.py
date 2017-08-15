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
