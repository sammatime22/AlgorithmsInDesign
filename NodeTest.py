import unittest


class Node:

    item = None

    next = None

    def __init__(self, item):
        self.item = item


class TestCases(unittest.TestCase):

    def test_node_instantiation(self):
        node = Node(20)

        assert node.item is 20 and node.next is None

    def test_linked_list(self):
        node_a = Node(10)
        node_b = Node(20)

        node_a.next = node_b

        assert node_a.item is 10 and node_a.next.item is 20

    def test_insertion_of_node(self):
        node_a = Node(10)
        node_b = Node(20)

        node_a.next = node_b

        node_c = Node(30)
        node_a.next = node_c
        node_c.next = node_b

        assert node_a.item is 10 and node_a.next.item is 30 and node_a.next.next.item is 20
