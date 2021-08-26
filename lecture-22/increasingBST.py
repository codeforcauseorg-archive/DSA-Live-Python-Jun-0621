# https://leetcode.com/problems/increasing-order-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def increasingBST(self, root):
        self.head = None
        self.tail = None

        self.increasingBSTRec(root)

        return self.head

    def increasingBSTRec(self, node):
        if not node:
            return

        self.increasingBSTRec(node.left)

        gen_node = TreeNode(node.val)

        if not self.head:
            self.head = gen_node
        else:
            self.tail.right = gen_node

        self.tail = gen_node

        self.increasingBSTRec(node.right)

