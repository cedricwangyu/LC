# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.p = []
        def helper(node, lev):
            if lev < len(self.p): self.p[lev].append(node.val)
            else: self.p.append([node.val])
            if node.left: helper(node.left, lev + 1)
            if node.right: helper(node.right, lev + 1)
        if root: helper(root, 0)
        return self.p