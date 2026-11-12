# Problem: Implement Stack using Arrays
# Approach: Use a Python list
# Time Complexity: Push O(1) amortized, Pop O(1), Peek O(1)
# Space Complexity: O(n)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())   
print(s.peek())  