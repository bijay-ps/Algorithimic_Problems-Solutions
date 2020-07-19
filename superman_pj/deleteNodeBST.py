# problem : https://leetcode.com/problems/delete-node-in-a-bst/
# Delete node from BST and return the updated root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        current = root
        parent = None
        while current != None:
            if key < current.val:
                parent = current
                current = current.left
            elif key > current.val:
                parent = current
                current = current.right
            elif key == current.val:
                # we found the element. Now we have three possibilities
                if current.right == None:
                    # Scenario 1: No right child
                    if parent == None:
                        # we are removing root node
                        root = current.left
                    elif current.val < parent.val:
                        parent.left = current.left
                    elif current.val > parent.val:
                        parent.right = current.left

                elif current.right.left == None:
                    # Scenario 2: Right child which doesn't have left child
                    current.right.left = current.left
                    if parent == None:
                        root = current.right
                    elif current.val < parent.val:
                        parent.left = current.right
                    elif current.val > parent.val:
                        parent.right = current.right

                else:
                    # Scenario 3: Right child that has a left child
                    # find the leftmost element and its leftmost parent
                    leftmost = current.right.left
                    leftmost_parent = current.right
                    while leftmost.left != None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    # shift leftmost subtree to its parent
                    leftmost_parent.left = leftmost.right
                    leftmost.left = current.left
                    leftmost.right = current.right

                    if parent == None:
                        root = leftmost
                    elif current.val < parent.val:
                        parent.left = leftmost
                    elif current.val > parent.val:
                        parent.right = leftmost
                return root
        return root


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


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

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys
    import io

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            line = next(lines)
            key = int(line)

            ret = Solution().deleteNode(root, key)

            out = treeNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
