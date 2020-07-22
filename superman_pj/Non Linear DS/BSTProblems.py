# Binary Search Tree implementation with basic operations
import collections

nodes = []


class BST:
    root = None

    class Node:
        left_child = None
        right_child = None

        def __init__(self, value):
            self.value = value

    def insert(self, value):
        new_node = self.Node(value)
        if self.root == None:
            self.root = new_node
            return self
        current = self.root
        while True:
            if value < current.value:
                if current.left_child == None:
                    current.left_child = new_node
                    break
                current = current.left_child
            else:
                if current.right_child == None:
                    current.right_child = new_node
                    break
                current = current.right_child
        return self

    def remove(self, value):
        if self.root == None:
            return False
        current = self.root
        parent = None
        while current != None:
            if value < current.value:
                parent = current
                current = current.left_child
            elif value > current.value:
                parent = current
                current = current.right_child
            elif value == current.value:
                # we found the element. Now we have three possibilities
                if current.right_child == None:
                    # Scenario 1: No right child
                    if parent == None:
                        # we are removing root node
                        self.root = current.left_child
                    elif current.value < parent.value:
                        parent.left_child = current.left_child
                    elif current.value > parent.value:
                        parent.right_child = current.left_child

                elif current.right_child.left_child == None:
                    # Scenario 2: Right child which doesn't have left child
                    current.right_child.left_child = current.left_child
                    if parent == None:
                        self.root = current.right_child
                    elif current.value < parent.value:
                        parent.left_child = current.right_child
                    elif current.value > parent.value:
                        parent.right_child = current.right_child

                else:
                    # Scenario 3: Right child that has a left child
                    # find the leftmost element and its leftmost parent
                    leftmost = current.right_child.left_child
                    leftmost_parent = current.right_child
                    while leftmost.left_child != None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left_child

                    # shift leftmost subtree to its parent
                    leftmost_parent.left_child = leftmost.right_child
                    leftmost.left_child = current.left_child
                    leftmost.right_child = current.right_child

                    if parent == None:
                        self.root = leftmost
                    elif current.value < parent.value:
                        parent.left_child = leftmost
                    elif current.value > parent.value:
                        parent.right_child = leftmost
                return True
        return False

    def find(self, value) -> bool:
        if self.root == None:
            return False
        current = self.root
        while current != None:
            if value < current.value:
                current = current.left_child
                continue
            elif value > current.value:
                current = current.right_child
                continue
            else:
                return True
        return False

    # https://leetcode.com/problems/same-tree/
    def isSameTree(self, p: Node, q: Node) -> bool:
        if p == None and q == None:
            return True
        if p != None and q != None:
            return p.value == q. value and self.isSameTree(p.left_child, q.left_childft) and self.isSameTree(p.right_childht, q.right_childht)
        return False

    # https://leetcode.com/problems/validate-binary-search-tree
    # use recursion to compare each node is within the range of accepted values
    def isValidBST(self, root) -> bool:
        return self.isValidNode(root, float('-inf'), float('inf'))

    def isValidNode(self, root, min, max):
        if root == None:
            return True
        if root.val < min or root.val > max:
            return False
        return self.isValidNode(root.left, min, root.val - 1) and self.isValidNode(root.right, root.val + 1, max)

    # https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

    def findSecondMinimumValue(self, root):
        self.ans = float('inf')
        min1 = root.value

        def dfs(node):
            if node:
                if min1 < node.value < self.ans:
                    self.ans = node.value
                elif node.value == min1:
                    dfs(node.left_child)
                    dfs(node.right_child)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1


def heightofTree(root) -> int:
    if root == None:
        return -1
    if root.left_child == None and root.right_child == None:
        return 0

    return 1 + max(heightofTree(root.left_child), heightofTree(root.right_child))


def getNodesatDistance(root, distance):
    if root != None:
        if distance == 0:
            nodes.append(root.val)
            return
        getNodesatDistance(root.left, distance - 1)
        getNodesatDistance(root.right, distance - 1)


def levelOrderTraversal(root):
    temp = []
    for i in range(1, heightofTree(root) + 1):
        getNodesatDistance(root, i)
        for val in nodes:
            temp.append(val)
    return temp


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.value) + ", "
        queue.append(node.left_child)
        queue.append(node.right_child)
    return "[" + output[:-2] + "]"


if __name__ == "__main__":
    tree = BST()
    tree.insert(2)
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(7)
    print(heightofTree(tree.root))
