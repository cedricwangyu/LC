# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, curr_max):
            if node is None: return
            if node.val >= curr_max: self.res, curr_max = self.res + 1, node.val
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)
        dfs(root, -10**4)
        return self.res
