# Problem:
# Group odd-positioned nodes followed by even-positioned nodes.
#
# Approach:
# Maintain odd and even pointers.
# Link odd-positioned nodes together and even-positioned nodes together.
# Connect the end of the odd list to the head of the even list.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def odd_even_list(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


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

head = odd_even_list(head)
print_list(head)