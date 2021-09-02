# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(left, right):
            if left > right: return [None,]
            trees = []
            for i in range(left, right+1):
                left_tree, right_tree = helper(left, i-1), helper(i+1, right)
                for l in left_tree:
                    for r in right_tree:
                        curr = TreeNode(i)
                        curr.left, curr.right = l, r
                        trees.append(curr)
            return trees
        return helper(1, n)
