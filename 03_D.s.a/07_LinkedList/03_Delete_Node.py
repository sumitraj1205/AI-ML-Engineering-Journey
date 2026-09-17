# Problem:
# Delete a node containing a given value from a Linked List.
#
# Approach:
# If the head contains the value, move the head to the next node.
# Otherwise, traverse the list and find the previous node.
# Connect the previous node directly to the node after the target.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node(head, value):
    if head is None:
        return None

    if head.data == value:
        return head.next

    current = head

    while current.next:
        if current.next.data == value:
            current.next = current.next.next
            return head

        current = current.next

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
head.next.next.next = Node(40)

head = delete_node(head, 30)

print_linked_list(head)