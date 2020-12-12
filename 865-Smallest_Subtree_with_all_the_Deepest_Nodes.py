# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node is None: return None, 0
            leftlev = rightlev = 0
            left = right = None
            if node.left: left, leftlev = helper(node.left)
            if node.right: right, rightlev = helper(node.right)
            if leftlev > rightlev: return left, leftlev + 1
            elif leftlev < rightlev: return right, rightlev + 1
            else: return node, leftlev + 1
        
        Node, Lev = helper(root)
        return Node
        