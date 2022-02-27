# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        levels= []
        def dfs(node, level, num):
            if node is None: return
            if level >= len(levels):
                levels.append([num, num])
            elif num < levels[level][0]:
                levels[level][0] = num
            else:
                levels[level][1] = num
            dfs(node.left, level+1, 2*num)
            dfs(node.right, level+1, 2*num+1)
        
        dfs(root, 0, 1)
        return max(r - l + 1 for l, r in levels)
                