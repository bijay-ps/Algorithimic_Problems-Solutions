
# problem : https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
# https://leetcode.com/problems/implement-queue-using-stacks/

# implement queue operations using two stacks
class Node:
    next = None

    def __init__(self, value):
        self.value = value


class Stack:
    def __init__(self):
        self.top = self.bottom = None

    def peek(self):
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = self.bottom = new_node
        else:
            hold_top = self.top
            self.top = new_node
            self.top.next = hold_top

        return self

    def pop(self):
        hold_top = self.top
        if self.top == self.bottom:
            self.top = self.bottom = None
        else:
            self.top = self.top.next
        return hold_top.value


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.enqueue_stack.push(x)
        return self

    def dequeue(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.dequeue_stack.top != None:
            return self.dequeue_stack.pop()
        else:
            current = self.enqueue_stack.top
            while current != None:
                self.dequeue_stack.push(self.enqueue_stack.pop())
                current = current.next
            hold_front = self.dequeue_stack.pop()

        return hold_front

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.dequeue_stack.top != None:
            return self.dequeue_stack.peek()
        else:
            current = self.enqueue_stack.top
            while current != None:
                self.dequeue_stack.push(self.enqueue_stack.pop())
                current = current.next
            hold_front = self.dequeue_stack.peek()

        return hold_front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.dequeue_stack.top == None and self.enqueue_stack.top == None


if __name__ == "__main__":
    myqueue = MyQueue()
    total_queries = int(input())
    while total_queries:
        query = input().split()
        if int(query[0]) == 1:
            myqueue.enqueue(int(query[1]))
        elif int(query[0]) == 2:
            myqueue.dequeue()
        elif int(query[0]) == 3:
            print(myqueue.peek())
        total_queries -= 1
