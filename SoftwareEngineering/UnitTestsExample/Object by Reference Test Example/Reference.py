import unittest


class Node:

    item = None

    next = None

    def __init__(self, item):
        self.item = item


def set_value_to_five(node):
    node.item = 5
    return node


class TestCases(unittest.TestCase):

    def testNodeValueSetToFive(self):
        new_node = Node(50)
        set_value_to_five(new_node)
        assert 5 == new_node.item

if __name__ == "__init__":
    unittest.main()
