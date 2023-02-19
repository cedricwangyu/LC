# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def dfs(node=root, level=0):
            if len(self.res) <= level:
                self.res.append([node.val])
            else:
                self.res[level].append(node.val)
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        if root:
            dfs()
        else:
            return
        
        for i in range(1, len(self.res), 2):
            self.res[i].reverse()
        
        return self.res