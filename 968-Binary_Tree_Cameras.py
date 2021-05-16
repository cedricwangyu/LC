# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def df(node):
            if node is None: return 0
            s = max(df(node.left), df(node.right))
            if s == 0: return 3
            elif s == 3: 
                self.res += 1
                return 2
            elif s == 2: return 1
            elif s == 1: return 3
        return self.res if df(root) < 3 else self.res + 1
