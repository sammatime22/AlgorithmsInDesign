class LinkedList:
    """
    A class of representing the classical "Linked List" datatype, implementing the algorithms typically seen within a
    Linked List.
    """
    head = None

    is_empty = True

    def append_element(self, element):
        """
        A function that allows the user to append an element.

        :param element: The element to be appended
        """
        if self.is_empty:
            self.is_empty = False
            self.head = element
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = element

    def remove_element(self, position):
        """
        Allows the user to remove an element from the list.

        :param position: The position of the element which is to be removed
        :return: The element removed from the list
        """
        if self.is_empty:
            return None

        pointer = self.head

        if position == 0:
            self.head = pointer.next
            pointer.next = None
            return pointer

        reference = None

        for i in range(0, position):
            reference = pointer
            pointer = pointer.next

        reference.next = pointer.next
        pointer.next = None
        return pointer

    def reverse_elements(self):
        """
        Reverses the list.
        """
        pointer_a = self.head
        if pointer_a is None:
            return

        pointer_b = pointer_a.next
        pointer_a.next = None
        if pointer_b is None:
            self.head = pointer_b
            self.head.next = pointer_a

        while pointer_b is not None:
            pointer_c = pointer_b.next
            pointer_b.next = pointer_a
            pointer_a = pointer_b
            pointer_b = pointer_c

        self.head = pointer_a

    def insert_element(self, position, element):
        """
        Inserts an element into the list.

        :param position: The position to which the element should be inserted
        :param element: The element to be inserted
        """
        pointer = self.head

        if position == 0:
            element.next = pointer
            self.head = element
            return

        for i in range(0, position - 1):
            pointer = pointer.next
        element.next = pointer.next
        pointer.next = element
