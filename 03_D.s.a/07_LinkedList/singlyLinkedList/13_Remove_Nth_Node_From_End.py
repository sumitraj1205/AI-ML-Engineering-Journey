# Problem:
# Remove the nth node from the end of a linked list.
#
# Approach:
# Create a dummy node before the head.
# Move fast n steps ahead.
# Move fast and slow together until fast reaches the last node.
# Delete the node after slow.
# Return dummy.next to handle deletion of the head.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(n):
        if fast.next is None:
            return head  # Invalid n
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


def print_list(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = remove_nth_from_end(head, 2)
print_list(head)