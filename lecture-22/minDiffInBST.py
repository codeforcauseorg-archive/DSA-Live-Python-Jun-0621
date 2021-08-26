# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        [minC, minB] = self.minDiffInBSTRec(root)
        return minB

    def minDiffInBSTRec(self, node, direction="root"):

        if (not node.left) and (not node.right):
            return [None, None]

        [minC, minB] = [None, None]

        if node.left:
            [leftC, leftB] = self.minDiffInBSTRec(node.left, "left")

            gap = node.val - node.left.val

            if leftC:
                if abs(leftC) > abs(leftC + gap):
                    leftC = (leftC + gap)
                leftB = min(abs(leftC), leftB)
            else:
                [leftC, leftB] = [gap, gap]

            if direction == "right":
                minC = leftC

            minB = leftB

        if node.right:
            [rightC, rightB] = self.minDiffInBSTRec(node.right, "right")

            gap = node.right.val - node.val

            if rightC:
                if abs(rightC) > abs(rightC + gap):
                    rightC = (rightC + gap)
                rightB = min(abs(rightC), rightB)
            else:
                [rightC, rightB] = [gap, gap]

            if direction == "left":
                minC = rightC

            if minB:
                minB = min(minB, rightB)
            else:
                minB = rightB

        return [minC, minB]

