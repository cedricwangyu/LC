# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        min_level = 1
        level = [root]
        while(True):
            next_level = []
            for node in level:
                if node.left is None and node.right is None:
                    return min_level
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            
            level = next_level.copy()
            min_level += 1
        
        