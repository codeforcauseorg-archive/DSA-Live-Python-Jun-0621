# https://leetcode.com/problems/balance-a-binary-search-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        self.data = []
        self.balanceBSTRec(root)

        return self.generate_tree(self.data, 0, len(self.data) - 1)

    def balanceBSTRec(self, node):
        if not node:
            return

        self.balanceBSTRec(node.left)
        self.data.append(node)
        self.balanceBSTRec(node.right)

    def generate_tree(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        node = nums[mid]
        node.left = self.generate_tree(nums, start, mid - 1)
        node.right = self.generate_tree(nums, mid + 1, end)

        return node

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Node(TreeNode):
#
#     def __init__(self, value, left=None, right=None):
#         super().__init__(value, left, right)
#         self.val = value
#         self.height = 1
#
#     @classmethod
#     def get_height(cls, node):
#         if node == None:
#             return 0
#
#         return node.height
#
#
# class BinarySearchTree:
#
#     def __init__(self):
#         self.__root = None
#
#     def insert(self, value):
#         self.__root = self.__add_node_rec(self.__root, value)
#
#     def __add_node_rec(self, node, value):
#         if node == None:
#             return Node(value)
#
#         if value < node.val:
#             node.left = self.__add_node_rec(node.left, value)
#         elif value > node.val:
#             node.right = self.__add_node_rec(node.right, value)
#         else:
#             node.count += 1
#
#         node.height = max(Node.get_height(node.left), Node.get_height(node.right)) + 1
#
#         node = BinarySearchTree.avl(node)
#         return node
#
#     @classmethod
#     def left_rotate(cls, root):
#         y = root
#         x = y.right
#         t2 = x.left
#
#         x.left = y
#         y.right = t2
#
#         y.height = max(Node.get_height(y.left), Node.get_height(y.right)) + 1
#         x.height = max(Node.get_height(x.left), Node.get_height(x.right)) + 1
#
#         return x
#
#     @classmethod
#     def right_rotate(cls, root):
#         x = root
#         y = x.left
#         t2 = y.right
#
#         y.right = x
#         x.left = t2
#
#         x.height = max(Node.get_height(x.left), Node.get_height(x.right)) + 1
#         y.height = max(Node.get_height(y.left), Node.get_height(y.right)) + 1
#
#         return y
#
#     @classmethod
#     def avl(cls, node):
#
#         if (Node.get_height(node.left) - Node.get_height(node.right)) > 1:
#             if (Node.get_height(node.left.left) - Node.get_height(node.left.right)) <= -1:
#                 node.left = BinarySearchTree.left_rotate(node.left)
#             node = BinarySearchTree.right_rotate(node)
#         elif (Node.get_height(node.left) - Node.get_height(node.right)) < -1:
#             if (Node.get_height(node.right.left) - Node.get_height(node.right.right)) >= 1:
#                 node.right = BinarySearchTree.right_rotate(node.right)
#             node = BinarySearchTree.left_rotate(node)
#
#         return node
#
#     def height_tree(self):
#         return Node.get_height(self.__root)
#
#     def get_root(self):
#         return self.__root
#
#
# class Solution:
#     def balanceBST(self, root: TreeNode) -> TreeNode:
#         tree = BinarySearchTree()
#         self.balanceBSTRec(root, tree)
#
#         return tree.get_root()
#
#     def balanceBSTRec(self, node, tree):
#         if not node:
#             return
#
#         self.balanceBSTRec(node.left, tree)
#         tree.insert(node.val)
#         self.balanceBSTRec(node.right, tree)
