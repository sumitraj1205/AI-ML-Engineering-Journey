# Problem:
# Reverse a Doubly Linked List.
#
# Approach:
# For every node, swap its prev and next pointers.
# After swapping, move to the new next pointer.
# Finally, update the head to the last processed node.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def reverse_dll(head):
    current = head
    new_head = None

    while current:
        # Swap prev and next
        current.prev, current.next = current.next, current.prev

        # Store the current node as the new head
        new_head = current

        # Move to the next node in the original list
        current = current.prev

    return new_head


def print_list(head):
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


head = Node(10)

node2 = Node(20)
head.next = node2
node2.prev = head

node3 = Node(30)
node2.next = node3
node3.prev = node2

node4 = Node(40)
node3.next = node4
node4.prev = node3

head = reverse_dll(head)

print_list(head)