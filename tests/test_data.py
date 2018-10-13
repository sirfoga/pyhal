# !/usr/bin/python
# coding: utf_8


"""Tests data module implementation"""

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
    """Tests linked list"""

    def test_build(self):
        """Asserts building linked list"""

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
        """Asserts insertions in linked list"""

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

        x = 98
        assert linked_list.insert_last(x)
        assert linked_list.get_tail().val == x  # last element

        y = 54
        assert linked_list.insert(y, 3)
        assert linked_list.get(3) == y

        assert linked_list.insert(x, linked_list.length() * 10)

    def test_removal(self):
        """Asserts insertions in linked list"""

        linked_list = LinkedList([])  # empty
        linked_list.insert_last(2)
        linked_list.insert_last(3)

        assert linked_list.remove_first()
        assert linked_list.remove_last()

        assert not linked_list.remove_first()
        assert linked_list.remove_last()
        assert linked_list.remove(4)

        max_tests = 10
        test_attempts = range(1, max_tests)
        for test in test_attempts:
            linked_list.insert(test)

        for test in test_attempts:
            print(linked_list)
            print(test)
            assert linked_list.remove(max_tests - 1 - test)

        assert linked_list.length() == 0

        linked_list.insert_last(1)
        linked_list.insert_last(2)
        linked_list.insert_last(3)
        assert linked_list.remove(1)

    def test_execute(self):
        """Asserts execution of function in linked list"""

        linked_list = LinkedList([])  # empty
        linked_list.insert_last(2)
        linked_list.insert_last(3)

        lst = linked_list.execute(lambda x: x * 2)
        assert set(lst) == {4, 6}
