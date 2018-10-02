# !/usr/bin/python3
# coding: utf-8


""" Tired of formatting ETA times? This is just for you """

from times import time


def get_time_eta(total_done, total, start_time):
    """
    :param total_done: int
        Item processed
    :param total: int
        Total number of items to process
    :param start_time: times
        Time of start processing items
    :return: times
        Time to go
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

        return {
            "done": int(total_done),
            "tot": int(total),
            "%": float("{0:.2f}".format(percentage)),
            "h": int(hours),
            "m": int(minutes),
            "s": int(seconds)
        }

    return {
        "done": int(total_done),
        "tot": int(total),
        "%": 0,
        "h": 0,
        "m": 0,
        "s": 0
    }


def print_time_eta(time_to_go, note=""):
    """
    :param time_to_go: {}
        Result of a call get_time_eta(...)
    :param note: str
        Notes to append to stdout
    :return: void
        Prints debug info to screen
    """

    print(
        str(note),
        str(time_to_go["done"]) + "/" + str(time_to_go["tot"]),
        "(" + str(time_to_go["%"]) + "%)",
        "ETA {:20.19}".format(
            str(time_to_go["h"]) + "h " + str(time_to_go["m"]) + "\' " + str(
                time_to_go["s"]) + "\""
        )
    )
