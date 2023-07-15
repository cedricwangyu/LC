# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(node=root):
            if self.res is not None:
                return [True, True]
            res = [False, False]
            if node:
                left1, left2 = dfs(node.left)
                right1, right2 = dfs(node.right)
                res = [left1 or right1, left2 or right2]
                if node == p:
                    res[0] = True
                if node == q:
                    res[1] = True
            
            if res[0] and res[1] and self.res is None:
                self.res = node
            return res
        dfs()
        return self.res
