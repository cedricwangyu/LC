# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if node is None: return -1
            l, r = dfs(node.left)+1, dfs(node.right)+1
            self.res = max(self.res, l+r)
            return max(l, r)
        dfs(root)
        return self.res
