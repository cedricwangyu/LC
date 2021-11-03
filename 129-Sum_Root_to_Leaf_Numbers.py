# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.curr, self.res = "", 0
        def dfs(node):
            self.curr += str(node.val)
            if node.left is None and node.right is None: self.res += int(self.curr)
            else:
                if node.left: dfs(node.left)
                if node.right: dfs(node.right)
            self.curr = self.curr[:-1]
        
        dfs(root)
        return self.res
