# Problem:
# Understand the basic structure of a Singly Linked List.
#
# Approach:
# A Linked List consists of nodes.
# Each node contains:
# 1. Data
# 2. A pointer to the next node
#
# The head stores the address of the first node.
# We can traverse the list by following the next pointer.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_linked_list(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

print_linked_list(head)