# https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):

        first = self.leafValue(root1, [])
        second = self.leafValue(root2, [])

        print(first, second)

        if len(first) != len(second):
            return False

        for index in range(len(first)):
            if first[index] != second[index]:
                return False

        return True

    def leafValue(self, node, solution):

        if (not node.left) and (not node.right):
            solution.append(node.val)
            return solution

        if node.left:
            self.leafValue(node.left, solution)

        if node.right:
            self.leafValue(node.right, solution)

        return solution