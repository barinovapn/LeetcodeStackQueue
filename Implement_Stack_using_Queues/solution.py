class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enq(self, x):
        new_node = Node(x)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def deq(self):
        if not self.front:
            return None
        val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def peek(self):
        if not self.front:
            return None
        return self.front.val

    def empty(self):
        return self.front is None


class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.enq(x)

        while not self.q1.empty():
            self.q2.enq(self.q1.deq())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.deq()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.empty()
