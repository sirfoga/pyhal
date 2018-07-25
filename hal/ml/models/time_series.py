#!/usr/bin/env python
# coding: utf-8


""" Multi-purpose prediction methods to be used in time-series. """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.tsa.arima_model as ar
import statsmodels.tsa.vector_ar.dynamic as dr
import statsmodels.tsa.vector_ar.var_model as vr
from statsmodels.tsa.stattools import adfuller


def test_stationary(time_series):
    """
    :param time_series: []
    :return: void
        Shows plot and checks for stationary series
    """

    rolling_mean = pd.rolling_mean(time_series, window=12)  # rolling stats
    rolling_std = pd.rolling_std(time_series, window=12)

    plt.plot(time_series, color='blue',
             label='Original')  # Plot rolling statistics:
    plt.plot(rolling_mean, color='red', label='Rolling Mean')
    plt.plot(rolling_std, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show()

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    df_test = adfuller(time_series, autolag='AIC')
    df_out = pd.Series(
        df_test[0:4],
        index=[
            'Test Statistic',
            'p-value',
            '# Lags Used',
            '# Observations Used'
        ]
    )
    for key, value in list(df_test[4].items()):
        df_out['Critical Value (%s)' % key] = value
    print(df_out)


def get_str_end(dates, end):
    """
    :param dates: []
        List of str date
    :param end: float
        End of prediction
    :return: str
        End of prediction
    """

    if end is None:
        end = np.datetime64(dates[-1])
        end += 1  # next day in database
        end = str(end)

    return end


def arma(dates, values, start=None, end=None, plot=False):
    """ Predict days values using ARMA algorithm.
    :param dates: list of str date
    :param values: list of float values
    :param start: start predicting in this day
    :param end: end of prediction
    :param plot: whether to plot or not values in graph """

    if start is None:
        start = dates[0]

    end = get_str_end(dates, end)
    y_series = pd.Series(values, index=dates)
    model = ar.ARMA(y_series, order=(2, 1, 0))
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

    end = get_str_end(dates, end)
    y_series = pd.Series(values, index=dates)
    model = ar.ARIMA(y_series, order=(2, 1, 0))
    model = model.fit(trend="nc", maxiter=1000, disp=False)
    return model.predict(start, end, dynamic=True)


def var(dates, values):
    """ Predict days values using ARIMA algorithm.
    :param dates: list of str date
    :param values: list of float values """

    y_series = pd.Series(values, index=dates)
    model = vr.VAR(y_series)
    model = model.fit(trend="nc")
    return model.forecast(y_series, steps=1)


def dynamic_var(dates, values):
    """ Predict days values using ARIMA algorithm.
    :param dates: list of str date
    :param values: list of float values """

    y_series = pd.Series(values, index=dates)
    model = dr.DynamicVAR(y_series, (2, 1, 0), trend="nc")
    return model.forecast(y_series)
