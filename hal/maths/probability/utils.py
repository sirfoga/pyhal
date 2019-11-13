# -*- coding: utf-8 -*-

""" Utils """

import numpy as np

def do_trials(experiment, trials):
    return [
        experiment()
        for _ in range(trials)
    ]


def get_stats(experiment, trials):
    results = do_trials(experiment, trials)
    mean, var = np.mean(results), np.std(results)
    std = np.power(var, 2)  # sigma squared
    return mean, std
