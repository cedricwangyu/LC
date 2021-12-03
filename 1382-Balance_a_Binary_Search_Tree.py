# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def tree2list(node):
            if node is None: return []
            return tree2list(node.left) + [node.val] + tree2list(node.right)
        self.L = tree2list(root)
        def construct(i, j):
            if i >= j: return None
            m = (i+j) // 2
            node = TreeNode(self.L[m])
            node.left, node.right = construct(i, m), construct(m+1, j)
            return node
        return construct(0, len(self.L))
