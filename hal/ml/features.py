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


""" Collection of methods to find weights of features and select the best
ones. """

from sklearn.feature_selection import SelectKBest, chi2, RFECV, RFE
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


def get_features(x_data, y_data, num_features):
    """ finds the optimal features """

    svc = SVC(kernel="linear", C=1)
    rfe = RFE(estimator=svc, n_features_to_select=num_features, step=1)
    rfe.fit(x_data, y_data)
    return rfe.ranking_
