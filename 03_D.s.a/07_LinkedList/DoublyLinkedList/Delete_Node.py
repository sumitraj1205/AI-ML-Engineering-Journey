# Problem:
# Delete a node containing a given value from a Doubly Linked List.
#
# Approach:
# Find the node containing the target value.
# Then connect its previous node to its next node.
# Also update the next node's prev pointer.
#
# Special case:
# If the node to delete is the head, move the head to the next node.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def delete_node(head, value):
    current = head

    while current:
        if current.data == value:

            # Deleting the head
            if current.prev is None:
                head = current.next

                if head:
                    head.prev = None

            else:
                current.prev.next = current.next

                if current.next:
                    current.next.prev = current.prev

            return head

        current = current.next

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

node4 = Node(40)
node3.next = node4
node4.prev = node3

head = delete_node(head, 30)

print_list(head)