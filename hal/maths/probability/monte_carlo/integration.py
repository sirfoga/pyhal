# -*- coding: utf-8 -*-

""" Monte Carlo integration """

import abc

import numpy as np

from hal.maths.probability.distribution.sampling import Pdf1D, Pdf2D


class MonteCarlo:
    def __init__(self, f):
        self.f = f

    @abc.abstractmethod
    def unpack_limits(self, limits):
        return None

    @abc.abstractmethod
    def integrate(self, limits, n):
        return 0

    @abc.abstractmethod
    def anal_mean_var(self, limits, n):
        return 0, 0

    @staticmethod
    def U(a, b):
        return np.random.uniform(a, b)

    @abc.abstractmethod
    def volume(self, limits):
        return 0


class MonteCarlo1D(MonteCarlo):
    def volume(self, limits):
        a, b = self.unpack_limits(limits)
        return b - a

    def unpack_limits(self, limits):
        a, b = limits  # just x-limits -> take first value
        return a, b

    def integrate(self, limits, n):
        a, b = self.unpack_limits(limits)

        def pdf():
            return self.U(a, b)

        samples = Pdf1D(pdf).sample(n)  # RV according to PDF
        ys = [self.f(sample) / (b - a) for sample in samples]  # f(X)
        raw_integration = sum(ys)
        return self.volume(limits) / n * raw_integration

    def anal_mean_var(self, limits, n):
        pdf = Pdf1D(self.f)
        mean, var = pdf.expected_value(limits), pdf.variance(limits)
        return mean, 1 / n * var


class MonteCarlo2D(MonteCarlo):
    def volume(self, limits):
        x_min, x_max, y_min, y_max = self.unpack_limits(limits)
        return (y_max - y_min) * (x_max - x_min)

    def unpack_limits(self, limits):
        x_min, x_max = limits[0]  # x-limit
        y_min, y_max = limits[1]  # y-limit
        return x_min, x_max, y_min, y_max

    def integrate(self, limits, n):
        x_min, x_max, y_min, y_max = self.unpack_limits(limits)

        def pdf():
            x = self.U(x_min, x_max)
            y = self.U(y_min, y_max)
            return y, x  # coordinates: first y like scipy

        samples = Pdf2D(pdf).sample(n)  # RV according to PDF
        zs = [self.f(*sample) for sample in samples]  # f(y, x)
        raw_integration = sum(zs)
        return self.volume(limits) / n * raw_integration

    def anal_mean_var(self, limits, n):
        pdf = Pdf2D(self.f)
        mean, var = pdf.expected_value(limits), pdf.variance(limits)
        return mean, 1 / n * var
