# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 1
        def helper(node):
            res = 1
            if node.left:
                candidate = helper(node.left)
                if node.left.val == node.val+1:
                    res = candidate + 1
            if node.right:
                candidate = helper(node.right)
                if node.right.val == node.val+1:
                    res = max(res, candidate+1)
            self.res = max(self.res, res)
            return res
        
        helper(root)
        return self.res
        
            