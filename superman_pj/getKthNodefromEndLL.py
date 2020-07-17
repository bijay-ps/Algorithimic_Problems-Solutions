
# problem : https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
# LinkedList implementation with basic operations
# getKthFromEnd function returns the Kth node from tail or end of linked list, where k=1 represents tail node

class LinkedList:
    head = None
    tail = None

    class Node:
        next = None

        def __init__(self, value):
            self.value = value

    def addLast(self, item):
        '''
        If LinkedList is empty, set both head and tail to new node
        Else set next of tail node to new node and tail as new node
        '''
        node = self.Node(item)
        if(self.__isListEmpty__()):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return self

    def addFirst(self, item):
        '''
        If LinkedList is empty, set both head and tail to new node
        Else set next of new node node to head and head as new node
        '''
        node = self.Node(item)
        if(self.__isListEmpty__()):
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        return self

    def insert(self, index, item):
        '''
        If LinkedList is empty, return list is empty.
        Else if list contains single element, call addFirst if insert index is 0.
        Else traverse through list to find insert index and keep track of previous var, then set next of previous to new node and set next of new node to current node.
        '''
        if(self.__isListEmpty__()):
            return "List is Empty"
        elif self.head == self.tail:
            return self.addFirst(item) if index == 0 else "Index out of range"

        curr_index = 0
        current = self.head
        previous = None

        while current != None:
            if index == curr_index:
                new_node = self.Node(item)
                previous.next = new_node
                new_node.next = current
                return self
            previous = current
            current = current.next
            curr_index += 1
        return "Index out of range"

    def indexof(self, item) -> int:
        '''
        Traverse through the list using index variable. find the item and return its index
        '''
        index = 0
        current = self.head
        while current != None:
            if current.value == item:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, item) -> bool:
        '''
        if index of item is positive, then element exists.
        '''
        return self.indexof(item) != -1

    def removeFirst(self):
        '''
        if empty list return empty msg.
        if list has single element, remove and set head, tail to None.
        else store second element to temp variable and set next of head to none to free up memory. then set head as second.
        '''
        if(self.__isListEmpty__()):
            return "List is Empty"
        elif self.head == self.tail:
            self.head = self.tail = None
            return "removed item. List is now empty"
        else:
            second = self.head.next
            self.head.next = None
            self.head = second
            return self

    def removeLast(self):
        '''
        if empty list return empty msg.
        if list has single element, remove and set head, tail to None.
        else traverse through list to find previous node of tail. set next of previous to none and set tail as previous
        '''
        if(self.__isListEmpty__()):
            return "List is Empty"
        elif self.head == self.tail:
            self.head = self.tail = None
            return "removed item. List is now empty"
        else:
            previous = self.__getPrevious__(self.tail)
            previous.next = None
            self.tail = previous

            return self

    def reverseList(self):
        '''
        if empty list return empty msg.
        else traverse through list keeping track of two pointers previous and current. then current will point to previous. keep next var to forward the loop. finally set head and tail 
        '''
        if(self.__isListEmpty__()):
            return "List is Empty"
        else:
            previous = self.head
            current = self.head.next

            while current != None:
                next = current.next
                current.next = previous
                previous = current
                current = next

            self.tail = self.head
            self.tail.next = None
            self.head = previous
            return self

    def getKthFromEnd(self, k):
        '''
        if empty list return empty msg.
        if list has single element, return single item
        else in single pass, keep track of first and current var. move first when distance between first and current is k-1
        here last node represents k = 1 and so on. 
        '''
        if(self.__isListEmpty__()):
            return "List is Empty"
        elif self.head == self.tail:
            return self.head.value if k == 1 else "K is out of range"
        else:
            current = self.head
            first = current
            distance = 0

            while current != None:
                if current == self.tail:
                    return first.value if distance == k-1 else "K is out of range"
                elif distance == k-1:
                    first = first.next
                current = current.next
                if distance < k-1:
                    distance += 1

    def __isListEmpty__(self) -> bool:
        return self.head == None

    def __getPrevious__(self, node):
        current = self.head
        while current != None:
            if current.next == node:
                return current
            current = current.next
        return None

    def __str__(self):
        current = self.head
        values = []
        while current != None:
            values.append(current.value)
            current = current.next
        return "List- " + str(values) + " ,head- " + str(self.head.value) + " ,tail- " + str(self.tail.value)


if __name__ == "__main__":
    myLL = LinkedList()
    myLL.addFirst(10)
    myLL.addLast(20)
    myLL.addLast(30)
    myLL.addLast(40)
    myLL.addLast(50)
    print(myLL.getKthFromEnd(3))
    pass
