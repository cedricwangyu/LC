# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if node1 is not None and node2 is not None and node1.val == node2.val:
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            elif node1 is None and node2 is None:
                return True
            else:
                return False
        
        return dfs(p, q)