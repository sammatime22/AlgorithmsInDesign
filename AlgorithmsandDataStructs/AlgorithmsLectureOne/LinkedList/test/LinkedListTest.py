import unittest
# Uncomment the .soln Linked List to see the LinkedListTests run!
# from AlgorithmsandDataStructs.AlgorithmsLectureOne.LinkedList.soln.LinkedList import LinkedList # My solution
# Create your own LinkedList file in the src folder and see if your Linked List passes!
from AlgorithmsandDataStructs.AlgorithmsLectureOne.LinkedList.src.LinkedList import LinkedList
from AlgorithmsandDataStructs.AlgorithmsLectureOne.Node.src.Node import Node


def list_builder_factory(elements):
    built_list = LinkedList()
    for element in elements:
        built_list.append_element(Node(element))
    return built_list


class LinkedListTests(unittest.TestCase):


    """
     This will test the user's defined 'append_element' method
    """
    def test_AppendingApplesTest(self):
        list = list_builder_factory(["Granny Smith", "Fuji", "Macintosh"])

        head_element = list.head

        assert head_element.item is "Granny Smith" # The first element
        assert head_element.next.item is "Fuji"
        assert head_element.next.next.item is "Macintosh" # The final element
        print("All AppendingApplesTests passed!")

    def test_RemovingRobotsTest(self):
        list = list_builder_factory(["MicroMouse", "Mars Rover", "iRobot"])

        removed_robot = list.remove_element(1)

        print(removed_robot.item)

        assert removed_robot.item is "Mars Rover"
        assert list.head.item is "MicroMouse"
        assert list.head.next.item is "iRobot"
        print("All RemovingRobotsTests passed!")

    def test_InsertingInstrumentsTest(self):
        list = list_builder_factory(["Bass", "Piano", "Cymbals"])

        list.insert_element(0, Node("Cajon"))
        list.insert_element(3, Node("Trumpet"))

        expected_instrument_order = ["Cajon", "Bass", "Piano", "Trumpet", "Cymbals"]

        pointer = list.head

        for instrument in expected_instrument_order:
            assert pointer.item == instrument
            pointer = pointer.next
        print("All InsertingInstrumentsTests passed!")

    def test_ReversingRevenuesTest(self):
        revenue_list = list_builder_factory([61.1, 4.366, 30.9]) # Random revenues in billions of USD

        revenue_list.reverse_elements()

        assert revenue_list.head.item == 30.9
        assert revenue_list.head.next.item == 4.366

        revenue_list.reverse_elements()
        assert revenue_list.head.item == 61.1
        print("All ReversingRevenuesTests passed!")
