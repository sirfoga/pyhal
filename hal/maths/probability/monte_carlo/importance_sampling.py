# -*- coding: utf-8 -*-

""" Importance sampling """

import numpy as np
import scipy.stats as ss

from hal.maths.probability.distribution.sampling import Pdf1D
from hal.maths.probability.monte_carlo.integration import MonteCarlo1D


class NormalImportanceSample(MonteCarlo1D):
    @staticmethod
    def N(mean, std):
        return np.random.normal(mean, std)

    def unpack_limits(self, config):
        a, b, mean, std = config  # just x-limits -> take first value
        return a, b, mean, std

    def integrate(self, config, n):
        a, b, mean, std = self.unpack_limits(config)

        def pdf():
            return self.N(mean, std)

        samples = Pdf1D(pdf).sample(n)  # RV according to PDF
        ys = [self.f(sample) for sample in samples]  # f(X)
        p = ss.uniform.pdf(samples, loc=0, scale=b - a)
        q = ss.norm.pdf(samples, loc=mean, scale=std)
        ws = p / q  # weighted
        raw_integration = sum(ys * ws)
        return 1 / n * raw_integration
