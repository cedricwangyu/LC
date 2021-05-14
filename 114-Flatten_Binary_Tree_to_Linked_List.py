# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def helper(node):
            if node.left is None and node.right is None: return node
            elif node.left is None and node.right: return helper(node.right)
            elif node.right is None and node.left:
                node.left, node.right = node.right, node.left
                return helper(node.right)
            else:
                l, r = helper(node.left), helper(node.right)
                l.right, node.left, node.right = node.right, None, node.left
                return r
        if root is None: return root
        helper(root)
        return root