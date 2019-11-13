# -*- coding: utf-8 -*-

""" Monte Carlo integration """

import abc

import numpy as np

from hal.maths.probability.distribution.sampling import Pdf1D, Pdf2D


class MonteCarlo:
    def __init__(self, f):
        self.f = f

    @abc.abstractmethod
    def integrate(self, config, n):
        return 0

    @abc.abstractmethod
    def anal_mean_var(self, config, n):
        return 0, 0

    @staticmethod
    def U(a, b):
        return np.random.uniform(a, b)

    @abc.abstractmethod
    def volume(self, config):
        return 0


class MonteCarlo1D(MonteCarlo):
    def volume(self, config):
        a, b = config
        return b - a

    def integrate(self, config, n):
        a, b = config

        def pdf():
            return self.U(a, b)

        samples = Pdf1D(pdf).sample(n)  # RV according to PDF
        ys = [self.f(sample) for sample in samples]  # f(X)
        raw_integration = sum(ys)
        return self.volume(config) / n * raw_integration


class MonteCarlo2D(MonteCarlo):
    def volume(self, config):
        x_min, x_max = config[0]  # x-limit
        y_min, y_max = config[1]  # y-limit
        return (y_max - y_min) * (x_max - x_min)

    def integrate(self, config, n):
        x_min, x_max = config[0]  # x-limit
        y_min, y_max = config[1]  # y-limit

        def pdf():
            x = self.U(x_min, x_max)
            y = self.U(y_min, y_max)
            return y, x  # coordinates: first y like scipy

        samples = Pdf2D(pdf).sample(n)  # RV according to PDF
        zs = [self.f(*sample) for sample in samples]  # f(y, x)
        raw_integration = sum(zs)
        return self.volume(config) / n * raw_integration
