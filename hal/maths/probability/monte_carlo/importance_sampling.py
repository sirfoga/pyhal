# -*- coding: utf-8 -*-

""" Importance sampling """

import numpy as np
import scipy.stats as ss

from hal.maths.probability.distribution.sampling import Pdf1D
from hal.maths.probability.monte_carlo.uniform import MonteCarlo


class NormalImportanceSample(MonteCarlo):
    @staticmethod
    def N(mean, std):
        return np.random.normal(mean, std)

    def volume(self, config):
        a, b, _, _ = config
        return b - a

    def integrate(self, config, n):
        a, b, mean, std = config

        def pdf():
            return self.N(mean, std)

        samples = Pdf1D(pdf).sample(n)  # RV according to PDF
        ys = [self.f(sample) for sample in samples]  # f(X)
        p = ss.uniform.pdf(samples, loc=0, scale=b - a)
        q = ss.norm.pdf(samples, loc=mean, scale=std)
        ws = p / q  # weighted
        raw_integration = sum(ys * ws)
        return 1 / n * self.volume(config) * raw_integration
