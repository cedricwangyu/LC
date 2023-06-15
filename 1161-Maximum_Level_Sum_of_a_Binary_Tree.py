# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.level = []
        def dfs(node=root, lev=0):
            if len(self.level) > lev:
                self.level[lev] += node.val
            else:
                self.level.append(node.val)
            if node.left:
                dfs(node.left, lev+1)
            if node.right:
                dfs(node.right, lev+1)
        
        dfs()
        res, curr = 0, self.level[0]
        for idx, val in enumerate(self.level):
            if val > curr:
                res, curr = idx, val
        
        return res + 1