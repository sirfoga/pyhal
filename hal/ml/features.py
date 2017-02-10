#!/usr/bin/env python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
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


""" Collection of methods to find weights of features and select the best ones. """

from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import SelectKBest, chi2, RFECV, RFE
from sklearn.svm import SVC


def select_k_best(x, y, k):
    """ select k best features in dataset """

    x_new = SelectKBest(chi2, k=k).fit_transform(x, y)
    return x_new


def get_best_features(x, y):
    """ finds the optimal number of features """

    svc = SVC(kernel="linear")
    rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(y, 2), scoring='log_loss')
    rfecv.fit(x, y)
    return rfecv.n_features_, rfecv.ranking_


def get_features(x, y, n_features_to_select):
    """ finds the optimal features """

    svc = SVC(kernel="linear", C=1)
    rfe = RFE(estimator=svc, n_features_to_select=n_features_to_select, step=1)
    rfe.fit(x, y)
    return rfe.ranking_
