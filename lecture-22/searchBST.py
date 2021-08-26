# https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, node, val):

        if not node:
            return None

        if node.val == val:
            return node

        return self.searchBST(node.left, val) or self.searchBST(node.right, val)
