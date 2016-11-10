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


""" Prediction methods based on classification algorithms. """


from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import naive_bayes


def extra_trees_classifier():
    return ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)


def random_forest():
    return RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)


def knn():
    """
        very fast and slightly more accurate than AdaBoost
    """

    return KNeighborsClassifier(n_neighbors=3, leaf_size=125)


def ada_boost():
    """
        fast, accurate but too uncertainty
    """

    return AdaBoostClassifier(DecisionTreeClassifier(max_depth=20), algorithm="SAMME.R", n_estimators=20)


def bayes_gauss():
    """ slower than svr but equally accuarte
    """

    return naive_bayes.GaussianNB()


def bayes_bernoulli():
    return naive_bayes.BernoulliNB()
