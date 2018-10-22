# -*- coding: utf-8 -*-


"""Tests hal.data.linked_list implementation"""

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


class TestNode:
    """Tests Node class"""

    pass  # todo auto generated method stub


class TestLinkedList:
    """Tests LinkedList class"""

    @staticmethod
    def test_get_head():
        """Tests hal.data.linked_list.LinkedList.get_head method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_get():
        """Tests hal.data.linked_list.LinkedList.get method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_get_tail():
        """Tests hal.data.linked_list.LinkedList.get_tail method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_length():
        """Tests hal.data.linked_list.LinkedList.length method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_insert_last():
        """Tests hal.data.linked_list.LinkedList.insert_last method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_insert_first():
        """Tests hal.data.linked_list.LinkedList.insert_first method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_insert():
        """Tests hal.data.linked_list.LinkedList.insert method"""

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

    @staticmethod
    def test_remove_first():
        """Tests hal.data.linked_list.LinkedList.remove_first method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_remove_last():
        """Tests hal.data.linked_list.LinkedList.remove_last method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_remove():
        """Tests hal.data.linked_list.LinkedList.remove method"""

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

    @staticmethod
    def test_to_lst():
        """Tests hal.data.linked_list.LinkedList.to_lst method"""

        tests = [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3, 4]
        ]

        for lst in tests:
            assert from_and_to_lst(lst) == lst

    @staticmethod
    def test_execute():
        """Tests hal.data.linked_list.LinkedList.execute method"""

        linked_list = LinkedList([])  # empty
        linked_list.insert_last(2)
        linked_list.insert_last(3)

        lst = linked_list.execute(lambda x: x * 2)
        assert set(lst) == {4, 6}

    @staticmethod
    def test_from_list():
        """Tests hal.data.linked_list.LinkedList.from_list method"""

        pass  # todo auto generated method stub
