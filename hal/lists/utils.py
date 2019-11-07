#!/usr/bin/env python
# coding: utf-8


def lst2str(lst, joiner=''):
    return joiner.join(str(item) for item in lst)
