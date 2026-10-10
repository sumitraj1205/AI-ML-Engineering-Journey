# Problem:
# Delete all occurrences of a given key in a Doubly Linked List.
#
# Approach:
# Traverse the list and check each node's value.
# If it matches the key, remove the node by updating
# both prev and next pointers.
# Update head if the first node is deleted.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def delete_all_occurrences(head, key):
    current = head

    while current:
        if current.data == key:
            if current.prev:
                current.prev.next = current.next
            else:
                head = current.next

            if current.next:
                current.next.prev = current.prev

        current = current.next

    return head


def print_list(head):
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


head = Node(2)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(2)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(4)
head.next.next.next.next.prev = head.next.next.next

head = delete_all_occurrences(head, 2)
print_list(head)