# Problem:
# Find the node where a cycle begins in a linked list.
#
# Approach:
# Use Floyd's Cycle Detection Algorithm.
# First find the meeting point of slow and fast.
# Reset slow to head, then move both pointers one step at a time.
# Their next meeting point is the cycle's starting node.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle_start(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle starts at node 2

start = detect_cycle_start(head)
print(start.data if start else None)