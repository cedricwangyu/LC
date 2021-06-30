# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(node):
            if node is None: return 0
            res = dfs(node.left) + dfs(node.right) + int(node in (p, q))
            if self.res is None and res == 2: self.res = node
            return res
        dfs(root)
        return self.res
