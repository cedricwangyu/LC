# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        p = {v: i for i, v in enumerate(inorder)}
        def helper(l, r):
            if l > r: return None
            root = TreeNode(preorder.pop(0))
            root.left = helper(l, p[root.val] - 1)
            root.right = helper(p[root.val] + 1, r)
            return root
        return helper(0, len(preorder) - 1)
