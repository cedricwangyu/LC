# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.curr, self.curr_sum, self.res = [], 0, []
        def dfs(node):
            self.curr.append(node.val)
            self.curr_sum += node.val
            if node.left is None and node.right is None and self.curr_sum == targetSum: self.res.append(self.curr.copy())
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            self.curr.pop()
            self.curr_sum -= node.val
        if root: dfs(root)
        return self.res
