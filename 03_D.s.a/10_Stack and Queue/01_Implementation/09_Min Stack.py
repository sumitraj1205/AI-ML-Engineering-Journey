# Problem: Implement Min Stack
# Approach: Use two stacks
# Time Complexity: Push O(1), Pop O(1), Top O(1), GetMin O(1)
# Space Complexity: O(n)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(val, self.min_stack[-1])
            )

    def pop(self):
        if not self.stack:
            return

        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return -1
        return self.min_stack[-1]

s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)

print(s.getMin())  # -3

s.pop()

print(s.top())     # 0
print(s.getMin())  # -2
