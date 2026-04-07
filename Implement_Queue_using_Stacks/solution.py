class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.val

    def empty(self):
        return self.top is None


class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()
