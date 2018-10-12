# !/usr/bin/python
# coding: utf_8


""" Tests linked list implementation """

from hal.data.linked_list import LinkedList
from hal.tests.utils import BatteryTests


def from_and_to_lst(lst):
    """
    :param: lst:
        List to parse
    :return: []
        Linked list to list
    """

    linked_list = LinkedList(lst)
    return linked_list.to_lst()


class TestLinkedList:
    """ Tests hal.files.models.FileSystem path handlers """

    def test_build(self):
        """
        :return: bool
            True iff FileSystem.fix_raw_path correctly handles raw paths
        """

        tests = [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3, 4]
        ]

        for lst in tests:
            assert from_and_to_lst(lst) == lst

    def test_insertion(self):
        """
        :return: bool
            True iff FileSystem.fix_raw_path correctly handles raw paths
        """

        test_attempts = range(1, 10)

        linked_list = LinkedList([])  # empty
        for test in test_attempts:
            tests = {
                linked_list.insert(test): True,
                linked_list.length(): test,
                linked_list.get_head().val: test,
                linked_list.get_tail().val: 1
            }
            BatteryTests(tests).assert_all()
