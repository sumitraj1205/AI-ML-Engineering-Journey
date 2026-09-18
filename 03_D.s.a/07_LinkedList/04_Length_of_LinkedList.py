# Problem:
# Find the length of a Linked List.
#
# Approach:
# Start from the head and traverse the complete list.
# Increase the count for every node.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_length(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Length:", find_length(head))