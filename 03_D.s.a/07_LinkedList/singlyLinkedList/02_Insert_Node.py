# Problem:
# Insert a new node at the end of a Linked List.
#
# Approach:
# If the list is empty, the new node becomes the head.
# Otherwise, traverse to the last node and connect the new node.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node

    return head


def print_linked_list(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = insert_at_end(head, 40)

print_linked_list(head)