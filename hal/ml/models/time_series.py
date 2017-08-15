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


""" Multi-purpose prediction methods to be used in time-series. """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.tsa.arima_model as ar
import statsmodels.tsa.vector_ar.dynamic as dr
import statsmodels.tsa.vector_ar.var_model as vr
from statsmodels.tsa.stattools import adfuller


def test_stationarity(timeseries):
    rolmean = pd.rolling_mean(timeseries,
                              window=12)  # rolling statistics
    rolstd = pd.rolling_std(timeseries, window=12)

    plt.plot(timeseries, color='blue',
             label='Original')  # Plot rolling statistics:
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show()

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4],
                         index=['Test Statistic', 'p-value', '# Lags Used',
                                '# Observations Used'])
    for key, value in list(dftest[4].items()):
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)


def arma(dates, values, start=None, end=None, plot=False):
    """ Predict days values using ARMA algorithm.
    :param dates: list of str date
    :param values: list of float values
    :param start: start predicting in this day
    :param end: end of prediction
    :param plot: whether to plot or not values in graph """

    if start is None:
        start = dates[0]

    if end is None:
        end = np.datetime64(dates[-1])
        end += 1  # next day in database
        end = str(end)

    y = pd.TimeSeries(values, index=dates)
    model = ar.ARMA(y, order=(2, 1, 0))
    model = model.fit(trend="nc", maxiter=1000, disp=False)

    graph = None
    if plot:  # returns also plot
        graph = model.plot_predict(start=start, end=end)
    return model.predict(start=start, end=end), graph


def arima(dates, values, start=None, end=None):
    """ Predict days values using ARIMA algorithm.
    :param dates: list of str date
    :param values: list of float values
    :param start: start predicting in this day
    :param end: end of prediction """

    if start is None:
        start = dates[0]

    if end is None:
        end = np.datetime64(dates[-1])
        end += 1  # next day in database
        end = str(end)

    y = pd.TimeSeries(values, index=dates)
    model = ar.ARIMA(y, order=(2, 1, 0))
    model = model.fit(trend="nc", maxiter=1000, disp=False)
    return model.predict(start, end, dynamic=True)


def var(dates, values, start=None, end=None):
    """ Predict days values using ARIMA algorithm.
    :param dates: list of str date
    :param values: list of float values
    :param start: start predicting in this day
    :param end: end of prediction """

    if start is None:
        start = dates[0]

    if end is None:
        end = np.datetime64(dates[-1])
        end += 1  # next day in database
        end = str(end)

    y = pd.TimeSeries(values, index=dates)
    model = vr.VAR(y)
    model = model.fit(trend="nc")
    return model.predict(start=start, end=end)


def dynamic_var(dates, values, start=None, end=None):
    """ Predict days values using ARIMA algorithm.
    :param dates: list of str date
    :param values: list of float values
    :param start: start predicting in this day
    :param end: end of prediction """

    if start is None:
        start = dates[0]

    if end is None:
        end = np.datetime64(dates[-1])
        end += 1  # next day in database
        end = str(end)

    y = pd.TimeSeries(values, index=dates)
    model = dr.DynamicVAR(y, (2, 1, 0))
    model = model.fit(trend="nc")
    return model.predict(start=start, end=end)
