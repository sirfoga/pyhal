# -*- coding: utf-8 -*-

"""Profile models"""

import time


class Timer(object):
    def __enter__(self):
        self.__start = time.time()

    def __exit__(self, exception_type, exception_value, traceback):
        self.__finish = time.time()

    def elapsed_time(self):
        """Calculates elapsed time

        :return: seconds elapsed since start
        """
        return self.__finish - self.__start
