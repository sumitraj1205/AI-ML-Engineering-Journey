# Problem:
# Find the middle node of a singly linked list.
#
# Approach:
# Use the Tortoise and Hare method.
# Slow moves one step and fast moves two steps.
# When fast reaches the end, slow is at the middle.
# For an even-length list, return the second middle node.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

middle = find_middle(head)
print(middle.data if middle else None)