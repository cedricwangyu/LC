# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        self.s = set()
        def dfs(node):
            if node is None: return 0
            res = node.val + dfs(node.left) + dfs(node.right)
            self.s.add(res)
            return res
        total = root.val + dfs(root.left) + dfs(root.right)
        return True if total % 2 == 0 and total // 2 in self.s else False
