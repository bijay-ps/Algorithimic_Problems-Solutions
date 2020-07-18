# Implementation of Stack using Arrays/Lists. Lists already support stack operations except peek
def peek(list):
    return list[len(list)-1]
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)
# print(stack.pop())
# print(stack)
# print(peek(stack))
# print(stack)

# Implementation of Stack using LinkedList


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
        if self.top == None:
            return "Stack is empty"
        hold_top = self.top
        if self.top == self.bottom:
            self.top = self.bottom = None
        else:
            self.top = self.top.next
        return hold_top.value

    def __str__(self):
        current = self.top
        values = []
        while current != None:
            values.append(current.value)
            current = current.next
        return "Stack is empty" if values == [] else "Stack- " + str(values) + " ,top- " + str(self.top.value) + " ,bottom- " + str(self.bottom.value)


# Implementation of Queue using Arrays/Lists. We keep track of two pointers front and rear. we enqueue using rear and deque using front.
# then we use circular array concept to avoid index out of range error. so rear = (rear + 1) % len(arr)

# Implementation of Queue using LinkedLists.
class Queue:
    def __init__(self):
        self.front = self.rear = None

    def peek(self):
        return self.front.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear == None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        return self

    def dequeue(self):
        if self.front == None:
            return "Queue is empty"
        hold_front = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return hold_front.value

    def __str__(self):
        current = self.front
        values = []
        while current != None:
            values.append(current.value)
            current = current.next
        return "Queue is empty" if values == [] else "Queue- " + str(values) + " ,front- " + str(self.front.value) + " ,rear- " + str(self.rear.value)


# Implementation of Queue using Stacks.

class QueueUsingStacks:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, value):
        self.enqueue_stack.push(value)
        return self

    def dequeue(self):
        if self.dequeue_stack.top == None and self.enqueue_stack.top == None:
            return "Queue is empty"
        elif self.dequeue_stack.top != None:
            return self.dequeue_stack.pop()
        else:
            current = self.enqueue_stack.top
            while current != None:
                self.dequeue_stack.push(self.enqueue_stack.pop())
                current = current.next
            hold_front = self.dequeue_stack.pop()

        return hold_front

    def __str__(self):
        current = self.enqueue_stack.top
        values = []
        while current != None:
            values.append(current.value)
            current = current.next
        current = self.dequeue_stack.top
        while current != None:
            values.append(current.value)
            current = current.next
        values.reverse()
        #front = self.enqueue_stack.top.value
        #rear = self.dequeue_stack.bottom.value if self.dequeue_stack.bottom != None else self.enqueue_stack.bottom.value
        return "Queue is empty" if values == [] else "Queue- " + str(values)
        #+ " ,front- " + str(front) + " ,rear- " + str(rear)


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def peek(self):
        return self.front.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear == None:
            self.front = self.rear = new_node
            return self
        current = self.front
        previous = None
        while current != None:
            if value <= current.value:
                if current == self.front:
                    new_node.next = self.front
                    self.front = new_node
                    return self
                elif current == self.rear:
                    self.rear.next = new_node
                    self.rear = new_node
                    return self
                else:
                    previous.next = new_node
                    new_node.next = current
                    return self

            previous = current
            current = current.next
        self.rear.next = new_node
        self.rear = new_node
        return self

    def dequeue(self):
        if self.front == None:
            return "Queue is empty"
        hold_front = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return hold_front.value

    def __str__(self):
        current = self.front
        values = []
        while current != None:
            values.append(current.value)
            current = current.next
        return "Queue is empty" if values == [] else "Queue- " + str(values) + " ,front- " + str(self.front.value) + " ,rear- " + str(self.rear.value)


if __name__ == "__main__":
    # myStack = Stack()
    # myStack.push(10)
    # myStack.push(20)
    # myStack.push(30)
    # print(myStack)
    # print(myStack.pop())
    # print(myStack.pop())
    # myStack.push(40)
    # print(myStack)
    # myqueue = Queue()
    # myqueue.enqueue(10)
    # myqueue.enqueue(20)
    # myqueue.enqueue(30)
    # print(myqueue)
    # print(myqueue.dequeue())
    # print(myqueue.dequeue())
    # myqueue.enqueue(40)
    # print(myqueue)

    # myqueue = QueueUsingStacks()
    # myqueue.enqueue(10)
    # myqueue.enqueue(20)
    # myqueue.enqueue(30)
    # print(myqueue)
    # print(myqueue.dequeue())
    # print(myqueue.dequeue())
    # print(myqueue)
    # myqueue.enqueue(40)
    # myqueue.enqueue(50)
    # print(myqueue)
    # print(myqueue.dequeue())
    # print(myqueue)

    myqueue = PriorityQueue()
    myqueue.enqueue(10)
    myqueue.enqueue(5)
    myqueue.enqueue(30)
    myqueue.enqueue(2)
    myqueue.enqueue(50)
    myqueue.enqueue(25)
    myqueue.enqueue(1)

    print(myqueue)
