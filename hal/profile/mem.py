# -*- coding: utf-8 -*-

""" Profile OS memory """

import gc
import os

import psutil


def get_memory_usage():
    """:return: float
        MB of memory used by this process

    # Arguments

    # Returns:
    """
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss
    return mem / (1024 * 1024)


def force_garbage_collect():
    """:return: void
        Releases memory used

    # Arguments

    # Returns:
    """
    gc.collect()
