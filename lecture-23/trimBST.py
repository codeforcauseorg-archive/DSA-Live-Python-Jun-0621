# Definition for a binary tree node.
# https://leetcode.com/problems/trim-a-binary-search-tree

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root, low, high):

        root = self.rangeSumRec(root, low, high)

        return root

    def rangeSumRec(self, node, low, high):

        if node == None:
            return None

        if node.val < low:
            node = node.right
            node = self.rangeSumRec(node, low, high)
        elif node.val > high:
            node = node.left
            node = self.rangeSumRec(node, low, high)
        else:
            node.left = self.rangeSumRec(node.left, low, high)
            node.right = self.rangeSumRec(node.right, low, high)

        return node
