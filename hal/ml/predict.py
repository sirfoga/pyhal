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


"""" General model to make prediction about everything. """


from sklearn.cross_validation import train_test_split


class BasePrediction(object):
    def __init__(self, model, rounds):
        object.__init__(self)

        self.model = model  # ml algorithm to use for prediction
        self.rounds = rounds  # number of times to make prediction (then get average)

    def train(self, x, y):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.67, random_state=None)  # cross-split
        self.model.fit(x_train, y_train)  # fit model
