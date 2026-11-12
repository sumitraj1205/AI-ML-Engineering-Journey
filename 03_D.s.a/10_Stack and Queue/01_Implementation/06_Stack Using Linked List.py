# Problem: Implement Stack using Linked List
# Approach: Use a singly linked list
# Time Complexity: Push O(1), Pop O(1), Peek O(1)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.top_node is None:
            return -1

        value = self.top_node.data
        self.top_node = self.top_node.next
        return value

    def peek(self):
        if self.top_node is None:
            return -1
        return self.top_node.data

    def is_empty(self):
        return self.top_node is None

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())   
print(s.peek())  