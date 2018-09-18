# !/usr/bin/python3
# coding: utf-8


""" Profile OS memory """

import gc
import os

import psutil


def get_memory_usage():
    """
    :return: float
        MB of memory used by this process
    """

    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss
    return mem / (1024 * 1024)


def force_garbage_collect():
    """
    :return: void
        Releases memory used
    """

    gc.collect()
