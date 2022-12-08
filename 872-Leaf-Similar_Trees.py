# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def next_leaf(node):
            if node:
                if node and not node.left and not node.right:
                    yield node.val

                yield from next_leaf(node.left)
                yield from next_leaf(node.right)

        return list(next_leaf(root1)) == list(next_leaf(root2))
        

        
        next_leaf(root1)