# -*- coding: utf-8 -*-

"""Wrappers to profile functions"""


def jd_time(func):
    """
    For debugging the execution time of a function.
    """

    def wrapper(*arg):
        start = time.time()
        print
        '# dec_time: enter', func.func_name
        try:
            return func(*arg)
        finally:
            print
            '# dec_time: exit {} ({} sec.)'.format(func.func_name,
                                                   time.time() - start)

    #
    return wrapper
