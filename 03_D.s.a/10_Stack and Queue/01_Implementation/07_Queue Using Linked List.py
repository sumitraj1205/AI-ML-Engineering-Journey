# Problem: Implement Queue using Linked List
# Approach: Maintain front and rear pointers
# Time Complexity: Enqueue O(1), Dequeue O(1), Peek O(1)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return -1

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        if self.front is None:
            return -1
        return self.front.data

    def is_empty(self):
        return self.front is None

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  
print(q.peek())     