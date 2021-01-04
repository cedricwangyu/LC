# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(node1, node2, target):
            res = None
            if node1 == target: return node2
            if node1.left: res = helper(node1.left, node2.left, target)
            if node1.right is not None and res is None: res = helper(node1.right, node2.right, target)
            return res
        return helper(original, cloned, target)