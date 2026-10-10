# Problem:
# Find the length of a loop in a linked list.
#
# Approach:
# Use slow and fast pointers to detect a cycle.
# When they meet, move one pointer around the loop
# until it returns to the meeting point.
# Count the number of steps.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_of_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1
            current = slow.next

            while current != slow:
                count += 1
                current = current.next

            return count

    return 0


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Loop length is 4

print(length_of_loop(head))