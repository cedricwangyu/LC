# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            res = [node.val, node.val, 1]
            if node.left:
                r = dfs(node.left)
                if r is None: res = None
                elif res is not None and r[1] < res[0]: res[0], res[2] = r[0], res[2] + r[2]
                else: res = None
            if node.right:
                r = dfs(node.right)
                if r is None: res = None
                elif res is not None and r[0] > res[1]: res[1], res[2] = r[1], res[2] + r[2]
                else: res = None
            if res is not None: self.ans = max(self.ans, res[2])
            return res
        
        if root: dfs(root)
        return self.ans        