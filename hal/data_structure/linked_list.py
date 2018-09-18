#!/usr/bin/env python
# coding: utf-8


""" Linked list implementation """


class Node:
    """ Node of a linked list """

    def __init__(self, val, next_node=None):
        """
        :param val: object
            Value of node
        :param next_node: Node
            Next node
        """

        self.val = val
        self.next_node = next_node  # the pointer initially points to nothing


class LinkedList:
    """ Models a linked list """

    def __init__(self, lst):
        """
        :param lst: []
            List of elements
        """

        self.head = LinkedList.from_list(lst)

    def get_head(self):
        """
        :return: Node
            Head of linked list
        """

        return self.head

    def get_tail(self):
        """
        :return: Node
            Tail of linked list
        """

        node = self.head
        last_node = self.head

        while node is not None:
            last_node = node
            node = node.next_node

        return last_node

    def length(self):
        """
        :return: int
            Length of linked list
        """

        item = self.head
        counter = 0

        while item is not None:
            counter += 1
            item = item.next_node

        return counter

    def append(self, val):
        """
        :param val: obj
            Object to insert
        :return: bool
            Appends element to last
        """

        return self.insert(val, self.length())

    def insert(self, val, at=0):
        """
        :param val: obj
            Object to insert
        :param at: int
            Index of insertion
        :return: bool
            True iff insertion completed successfully
        """

        if at < 0 or at > self.length():
            return False

        if at == 0:  # at beginning
            self.head = Node(val, next_node=self.head)
            return True

        counter = 0
        last_node = self.head
        current_node = self.head

        while current_node is not None and counter <= at:
            if counter == at:
                last_node.next_node = Node(val, current_node)
                return True

            last_node = current_node
            current_node = current_node.next_node
            counter += 1

        if current_node is None:  # append to last element
            last_node.next_node = Node(val, None)
            return True

        return False

    def remove_first(self):
        """
        :return: bool
            True iff head has been removed
        """

        if self.head.next_node is not None:
            self.head = self.head.next_node
            return True

        return False

    def remove_last(self):
        """
        :return: bool
            True iff last element has been removed
        """

        node = self.head

        while node is not None:
            if node.next_node.next_node is None:
                node.next_node = None  # get to last but one element
                return True

            node = node.next_node

        return False

    def remove(self, at):
        """
        :param at: int
            Index of removal
        :return: bool
            True iff removal completed successfully
        """

        if at < 0 or at > self.length():
            return False

        if at == 0:  # at beginning
            self.remove_first()

        if at == self.length():  # at end
            self.remove_last()

        counter = 0
        last_node = self.head
        current_node = self.head

        while current_node is not None and counter <= at:
            if counter == at:
                last_node.next_node = current_node.next_node  # remove current
                return True

            last_node = current_node
            current_node = current_node.next_node
            counter += 1

        return False

    def to_lst(self):
        """
        :return: []
            Cycle all items and puts them in a list
        """

        out = []
        node = self.head

        while node is not None:
            out.append(node.val)
            node = node.next_node

        return out

    def execute(self, func):
        """
        :param func: function
            Function to execute on each item
        :return: []
            Results of calling the function on each item
        """

        return [
            func(item) for item in self.to_lst()
        ]

    def __str__(self):
        lst = self.to_lst()
        lst = [
            str(node) for node in lst
        ]
        return " -> ".join(lst)

    @staticmethod
    def from_list(lst):
        """
        :param lst: []
            List of elements
        :return: Node
            Nodes from list
        """

        if not lst:
            return None

        head = Node(lst[0], None)

        if len(lst) == 1:
            return head

        head.next_node = LinkedList.from_list(lst[1:])
        return head


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5]
    l = LinkedList(lst1)

    print("insert 0 at 5")
    ok = l.insert(0, at=5)
    print(ok, l)

    print("removed first")
    ok = l.remove_first()
    print(ok, l)

    print("removed last")
    ok = l.remove_last()
    print(ok, l)

    print("removed at 2")
    ok = l.remove(2)
    print(ok, l)
