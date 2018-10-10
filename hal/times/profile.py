# -*- coding: utf-8 -*-

"""Tired of formatting ETA times? This is just for you """

from time import time


def get_time_eta(total_done, total, start_time):
    """Gets ETA

    :param total_done: items processed
    :param total: total # of items to process
    :param start_time: Time of start processing items
    :returns: Time to go

    """
    time_done = int(time()) - start_time
    try:
        speed = total_done / time_done
    except:
        speed = 0

    if time_done > 0 and speed > 0:
        total_to_go = total - total_done
        time_to_go = total_to_go / speed
        minutes, seconds = divmod(time_to_go, 60)
        hours, minutes = divmod(minutes, 60)
        percentage = total_done * 100.0 / total
    else:
        percentage = 0
        hours = 0
        minutes = 0
        seconds = 0

    return {
        "done": int(total_done),
        "tot": int(total),
        "%": float("{0:.2f}".format(percentage)),
        "h": int(hours),
        "m": int(minutes),
        "s": int(seconds)
    }
