# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res = float("Inf")
        def dfs(node, lo, hi):
            self.res = min(self.res, node.val - lo, hi - node.val)
            if node.left:
                dfs(node.left, lo, node.val)
            if node.right:
                dfs(node.right, node.val, hi)
        
        dfs(root, float("-Inf"), float("Inf"))
        return self.res
