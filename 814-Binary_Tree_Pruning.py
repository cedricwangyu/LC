# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None: return True
            l, r = dfs(node.left), dfs(node.right)
            if l: node.left = None
            if r: node.right = None
            if l and r and node.val == 0: return True
            else: return False
        if dfs(root): root = None
        return root
