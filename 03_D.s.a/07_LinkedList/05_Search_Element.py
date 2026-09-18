# Problem:
# Search for an element in a Linked List.
#
# Approach:
# Traverse the Linked List from the head.
# Compare every node's data with the target value.
# Return True if the element is found, otherwise return False.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search_element(head, target):
    current = head

    while current:
        if current.data == target:
            return True

        current = current.next

    return False


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(search_element(head, 30))
print(search_element(head, 50))