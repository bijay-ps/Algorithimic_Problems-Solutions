class MaxHeap:
    items = []

    def insert(self, value):
        self.items.append(value)
        # check if the newly added item is greater than its parent, which means it violates maxHeap property
        new_index = len(self.items) - 1  # the recent item inserted
        # if new item is greater than its parent item
        while new_index > 0 and self.items[new_index] > self.items[self.parent(new_index)]:
            # swap the new itema and its parent item
            self.items[new_index], self.items[self.parent(
                new_index)] = self.items[self.parent(new_index)], self.items[new_index]

            # new item has moved up so reassign the index and again check for maxHeap condition
            new_index = self.parent(new_index)

    def remove(self):
        if len(self.items) == 0:
            return "Heap is Empty"

        # remove the root item and replace it with last item
        removedItem = self.items[0]
        self.items[0] = self.items[len(self.items) - 1]
        self.items.pop()

        # bubble down operation while the root is smaller than both of its children.
        parent_index = 0
        while parent_index < len(self.items) and not self.isValidParent(parent_index):
            # bubble up the larger child to parent
            self.items[self.largerChildIndex(
                parent_index)], self.items[parent_index] = self.items[parent_index], self.items[self.largerChildIndex(parent_index)]
            parent_index = self.largerChildIndex(parent_index)

        return removedItem

    def largerChildIndex(self, index):
        if not self.leftChildIndex(index) < len(self.items):
            return index
        if not self.rightChildIndex(index) < len(self.items):
            return self.leftChildIndex(index)

        return self.leftChildIndex(index) if self.items[self.leftChildIndex(index)] > self.items[self.rightChildIndex(index)] else self.rightChildIndex(index)

    def isValidParent(self, index):
        if not self.leftChildIndex(index) < len(self.items):
            return True
        if not self.rightChildIndex(index) < len(self.items):
            return self.items[index] >= self.items[self.leftChildIndex(index)]

        return self.items[index] >= self.items[self.leftChildIndex(index)] and self.items[index] >= self.items[self.rightChildIndex(index)]

    def rightChildIndex(self, index):
        return index * 2 + 2

    def leftChildIndex(self, index):
        return index * 2 + 1

    def parent(self, index):
        return (index - 1) // 2


def heapifyArray(arr):
    lastParentIndex = len(arr)//2 - 1
    for i in range(lastParentIndex, -1, -1):
        heapify(arr, i)
    return arr


def heapify(arr, index):
    largerIndex = index
    leftIndex = index * 2 + 1
    rightIndex = index * 2 + 2
    if leftIndex < len(arr) and arr[leftIndex] > arr[largerIndex]:
        largerIndex = leftIndex
    if rightIndex < len(arr) and arr[rightIndex] > arr[largerIndex]:
        largerIndex = rightIndex
    if index == largerIndex:  # index is already greater than both child
        return

    arr[index], arr[largerIndex] = arr[largerIndex], arr[index]
    heapify(arr, largerIndex)

# get Kth largest item. convert arr to maxHeap and then remove items upto k-1. then remove root and return


def getKthMaxItem(arr, k):
    if k < 1 or k > len(arr):
        return "K is out of range of array"
    maxheap = MaxHeap()
    for i in arr:
        maxheap.insert(i)
    for i in range(0, k-1):
        maxheap.remove()
    return maxheap.remove()


if __name__ == "__main__":
    # heap = MaxHeap()
    # heap.insert(10)
    # heap.insert(5)
    # heap.insert(17)
    # heap.insert(4)
    # heap.insert(22)
    # print(heap.items)
    # print(heap.remove())
    # print(heap.items)
    nums = [5, 3, 8, 4, 1, 2]
    print(heapifyArray(nums))
    print(getKthMaxItem(nums, 7))
