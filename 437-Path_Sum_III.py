# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path, self.p, self.res = [0], defaultdict(int), 0
        self.p[0] = 1
        def dfs(node):
            if node is None: return
            self.path.append(node.val + self.path[-1])
            if self.p[self.path[-1] - targetSum] > 0: self.res += self.p[self.path[-1] - targetSum]
            self.p[self.path[-1]] += 1
            dfs(node.left)
            dfs(node.right)
            self.p[self.path[-1]] -= 1
            self.path.pop()
        dfs(root)
        return self.res