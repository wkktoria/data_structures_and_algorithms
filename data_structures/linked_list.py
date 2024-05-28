class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

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
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            previous_node = self.__traverse_to_index(index - 1)
            previous_node.next = previous_node.next.next
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
            print(f"{current_node.value} -> ", end="")
            current_node = current_node.next
        print(f"null (length: {self.length})")


linked_list = LinkedList(4)
linked_list.append(16)
linked_list.prepend(2)
linked_list.append(32)
linked_list.print()
linked_list.insert(2, 8)
linked_list.print()
