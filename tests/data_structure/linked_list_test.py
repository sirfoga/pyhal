# !/usr/bin/python
# coding: utf_8


""" Tests linked list implementation """

from unittest import TestCase, main

from data.linked_list import LinkedList


def from_and_to_lst(lst):
    """
    :param: lst:
        List to parse
    :return: []
        Linked list to list
    """

    linked_list = LinkedList(lst)
    return linked_list.to_lst()


class TestPaths(TestCase):
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
            self.assertEqual(from_and_to_lst(lst), lst)

    def test_insertion(self):
        """
        :return: bool
            True iff FileSystem.fix_raw_path correctly handles raw paths
        """

        tests = range(1, 10)

        linked_list = LinkedList([])  # empty
        for test in tests:
            self.assertTrue(linked_list.insert(test))
            self.assertEqual(linked_list.length(), test)

            self.assertEqual(linked_list.get_head().val, test)
            self.assertEqual(linked_list.get_tail().val, 1)


if __name__ == '__main__':
    main()
