# Problem:
# Understand the basic structure of a Doubly Linked List.
#
# Approach:
# Each node contains three parts:
# 1. Data
# 2. Pointer to the previous node
# 3. Pointer to the next node
#
# Unlike a Singly Linked List, a Doubly Linked List
# allows traversal in both directions.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_forward(head):
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

head = node1

print_forward(head)