# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(node=root):
            res = (-1, -1)
            if node:
                res = (helper(node.left)[1] + 1, helper(node.right)[0] + 1)
            self.res = max(self.res, res[0], res[1])
            return res
        helper()
        return self.res
        