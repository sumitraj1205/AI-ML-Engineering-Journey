# Problem:
# Find all pairs in a sorted Doubly Linked List
# whose sum equals the given target.
#
# Approach:
# Use two pointers: left at the head and right at the tail.
# If the sum is equal to target, store the pair and move both.
# If the sum is smaller, move left forward.
# If the sum is larger, move right backward.
#
# Time Complexity: O(n + p)
# Space Complexity: O(p)
# p = number of pairs stored in the result


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def find_pairs(head, target):
    if head is None:
        return []

    left = head
    right = head

    # Find the tail
    while right.next:
        right = right.next

    pairs = []

    while left != right and left.prev != right:
        total = left.data + right.data

        if total == target:
            pairs.append((left.data, right.data))
            left = left.next
            right = right.prev

        elif total < target:
            left = left.next

        else:
            right = right.prev

    return pairs


head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next

print(find_pairs(head, 5))