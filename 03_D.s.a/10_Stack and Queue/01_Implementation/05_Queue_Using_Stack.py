# Problem: Implement Queue using Stack
# Approach: Use two stacks
# Time Complexity: Enqueue O(1), Dequeue O(1) amortized
# Space Complexity: O(n)

class Queue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, x):
        self.input_stack.append(x)

    def dequeue(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(
                    self.input_stack.pop()
                )

        if not self.output_stack:
            return -1

        return self.output_stack.pop()

    def peek(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(
                    self.input_stack.pop()
                )

        if not self.output_stack:
            return -1

        return self.output_stack[-1]

    def empty(self):
        return not self.input_stack and not self.output_stack

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # 10
print(q.peek())     # 20