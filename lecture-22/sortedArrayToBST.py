# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.generate_tree(nums, 0, len(nums) - 1)

    def generate_tree(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        node = TreeNode(nums[mid])
        node.left = self.generate_tree(nums, start, mid - 1)
        node.right = self.generate_tree(nums, mid + 1, end)

        return node


