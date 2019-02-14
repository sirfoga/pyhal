#!/usr/bin/env python3
# coding: utf-8


""" Logging module """

import logging
import threading

LOG_THREAD_FORMAT = "thread-{} {}"  # when logging # threads
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
CUSTOM_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"

LOG_LEVEL = logging.DEBUG

LOGGER = logging.getLogger("hal")
LOGGER.setLevel(LOG_LEVEL)

STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setLevel(LOG_LEVEL)
STREAM_HANDLER.setFormatter(logging.Formatter(LOG_FORMAT))

LOGGER.addHandler(STREAM_HANDLER)


def get_logger():
    """Gets default logger

    :return: logger
    """
    return LOGGER


def log_message(*message):
    """Logs message

    :param message: message to log
    """
    logger = get_logger()
    logger.debug(" ".join(message))


def log_error(*error, cause=None):
    """Logs error

    :param error: error to log
    :param cause: (optional) cause of error
    """
    thread_id = threading.current_thread().ident
    text = " ".join(error)
    if cause:
        text += " due to " + str(cause)

    logger = get_logger()
    logger.error(LOG_THREAD_FORMAT.format(thread_id, text))


def get_custom_logger(logger_name):
    formatter = logging.Formatter(fmt=CUSTOM_LOG_FORMAT)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
