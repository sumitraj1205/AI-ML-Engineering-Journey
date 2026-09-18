# Problem:
# Design a singly Linked List with basic operations.
#
# Operations:
# 1. Get a node value by index
# 2. Add a node at the beginning
# 3. Add a node at the end
# 4. Add a node at a given index
# 5. Delete a node at a given index
#
# Approach:
# Use a Node class to store data and the next pointer.
# Use a LinkedList class to manage the head and perform operations.
#
# Time Complexity:
# get: O(n)
# add_at_head: O(1)
# add_at_tail: O(n)
# add_at_index: O(n)
# delete_at_index: O(n)
#
# Space Complexity: O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data

            count += 1
            current = current.next

        return -1

    def add_at_head(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def add_at_index(self, index, data):
        if index == 0:
            self.add_at_head(data)
            return

        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            return

        new_node = Node(data)

        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0

        while current.next and count < index - 1:
            current = current.next
            count += 1

        if current.next:
            current.next = current.next.next

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


linked_list = MyLinkedList()

linked_list.add_at_head(10)
linked_list.add_at_tail(30)
linked_list.add_at_index(1, 20)

linked_list.print_list()

print("Value at index 1:", linked_list.get(1))

linked_list.delete_at_index(1)

linked_list.print_list()