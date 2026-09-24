# Problem:
# Insert a new node at the end of a Doubly Linked List.
#
# Approach:
# If the list is empty, the new node becomes the head.
# Otherwise, traverse to the last node.
# Connect the new node using both next and prev pointers.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insert_at_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current

    return head


def print_list(head):
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


head = Node(10)

node2 = Node(20)
head.next = node2
node2.prev = head

node3 = Node(30)
node2.next = node3
node3.prev = node2

head = insert_at_end(head, 40)

print_list(head)