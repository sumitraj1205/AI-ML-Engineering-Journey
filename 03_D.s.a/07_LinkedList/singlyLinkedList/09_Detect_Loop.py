# Problem:
# Check whether a linked list contains a cycle.
#
# Approach:
# Move slow by one step and fast by two steps.
# If they meet, a cycle exists.
# If fast reaches None, there is no cycle.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next  # Creates a cycle

print(has_cycle(head))