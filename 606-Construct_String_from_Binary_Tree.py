# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = ""
        def dfs(node=root):
            self.res += str(node.val)
            if node.left or node.right:
                self.res += "("
                if node.left:
                    dfs(node.left)
                self.res += ")"
                if node.right:
                    self.res += "("
                    dfs(node.right)
                    self.res += ")"
        dfs()
        return self.res
        