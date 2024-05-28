class DoublyLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __init__(self, value):
        self.head = self.Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0:
            raise IndexError("Index cannot be negative")
        elif index >= self.length:
            raise IndexError(
                "Index cannot be greater than or equal to the length of the list"
            )

        if index == 0:
            self.prepend(value)
        elif index == self.length - 1:
            self.append(value)
        else:
            previous_node = self.__traverse_to_index(index - 1)
            new_node = self.Node(value)
            new_node.prev = previous_node
            previous_node.next.prev = new_node
            new_node.next = previous_node.next
            previous_node.next = new_node

            self.length += 1

    def remove(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        elif index >= self.length:
            raise IndexError(
                "Index cannot be greater than or equal to the length of the list"
            )

        if index == 0:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            previous_node = self.__traverse_to_index(index - 1)
            previous_node.next = previous_node.next.next
            if previous_node.next != None:
                previous_node.next.prev = previous_node
        self.length -= 1

    def __traverse_to_index(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        elif index >= self.length:
            raise IndexError(
                "Index cannot be greater than or equal to the length of the list"
            )

        current_index = 0
        current_node = self.head

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        return current_node

    def print(self):
        current_node = self.head
        while current_node != None:
            print(f"{current_node.value} <->", end=" ")
            current_node = current_node.next
        print(f"null (length: {self.length})")


doubly_linked_list = DoublyLinkedList(4)
doubly_linked_list.insert(0, 2)
doubly_linked_list.print()
doubly_linked_list.insert(1, 8)
doubly_linked_list.print()
doubly_linked_list.remove(1)
doubly_linked_list.print()
