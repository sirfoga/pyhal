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


""" Collection of models based on nn algorithms """


from sknn.mlp import Classifier, Convolution, Layer  # test only
# from sklearn.neural_network import MLPClassifier  # dev only


def convolution():
    return Classifier(layers=[Convolution("Rectifier", channels=8, kernel_shape=(3, 3)), Layer("Softmax")], learning_rate=0.02, n_iter=5)


def mpl():
    return None   # TODO: MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)  # dev only
