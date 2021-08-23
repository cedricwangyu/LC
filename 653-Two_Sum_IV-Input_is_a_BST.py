# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.p = set()
        def dfs(node):
            if node is None: return False
            if node.val in self.p: return True
            else:
                self.p.add(k - node.val)
                return dfs(node.left) or dfs(node.right)
        return dfs(root)