# Problem: Implement Queue using Arrays
# Approach: Use a list with a front pointer
# Time Complexity: Enqueue O(1) amortized, Dequeue O(1), Peek O(1)
# Space Complexity: O(n)

class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.front == len(self.queue):
            return -1

        value = self.queue[self.front]
        self.front += 1

        # Reset when queue becomes empty
        if self.front == len(self.queue):
            self.queue = []
            self.front = 0

        return value

    def peek(self):
        if self.front == len(self.queue):
            return -1
        return self.queue[self.front]

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  
print(q.peek())     