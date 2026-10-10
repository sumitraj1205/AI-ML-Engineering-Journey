# Problem:
# Remove duplicate values from a sorted Doubly Linked List.
#
# Approach:
# Traverse the list using current.
# If current and current.next contain the same value,
# remove current.next by updating the pointers.
# Otherwise, move current forward.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def remove_duplicates(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            duplicate = current.next
            current.next = duplicate.next

            if duplicate.next:
                duplicate.next.prev = current

        else:
            current = current.next

    return head


def print_list(head):
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


head = Node(1)
head.next = Node(1)
head.next.prev = head
head.next.next = Node(2)
head.next.next.prev = head.next
head.next.next.next = Node(3)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(3)
head.next.next.next.next.prev = head.next.next.next

head = remove_duplicates(head)
print_list(head)