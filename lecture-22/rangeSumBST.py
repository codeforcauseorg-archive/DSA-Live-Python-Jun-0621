# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        return self.rangeSumRec(root, low, high)

    def rangeSumRec(self, node, low, high):

        if node == None:
            return 0

        total = 0

        if (node.val >= low) and (node.val <= high):
            total += node.val

        if node.val > low:
            total += self.rangeSumRec(node.left, low, high)

        if node.val < high:
            total += self.rangeSumRec(node.right, low, high)

        return total

