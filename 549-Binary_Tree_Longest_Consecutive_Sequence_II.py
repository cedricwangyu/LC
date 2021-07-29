# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0
        self.m = float('-inf')
        def longConsecutiveHelper(root):
            if not root: return [0, 0]
            leftInc, leftDec, rightInc, rightDec, curInc, curDec = *longConsecutiveHelper(root.left), *longConsecutiveHelper(root.right), 1, 1
            if root.left:
                if root.val - root.left.val == -1: curInc = max(curInc, leftInc + 1)
                if root.val - root.left.val == 1: curDec = max(curDec, leftDec + 1)
            if root.right:
                if root.val - root.right.val == -1: curInc = max(curInc, rightInc + 1)
                if root.val - root.right.val == 1: curDec = max(curDec, rightDec + 1)
            curMax = curInc + curDec - 1
            self.m = max(self.m, curMax)
            return [curInc, curDec]
        longConsecutiveHelper(root)
        return self.m
