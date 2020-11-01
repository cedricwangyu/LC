# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def mnode(node):
            M = m = node
            if node.left is None and node.right is None:
                return M,m
            if node.left:
                Ml, ml = mnode(node.left)
                if Ml.val > M.val: M = Ml
                if ml.val < m.val: m = ml
            if node.right:
                Mr, mr = mnode(node.right)
                if Mr.val > M.val: M = Mr
                if mr.val < m.val: m = mr
            return M,m
        def helper(root, problem, ranges):
            if root.val < ranges[0].val or root.val > ranges[1].val:
                problem.append([root] + ranges)
                return
            
            if root.left: helper(root.left, problem, [ranges[0], root])
            if root.right: helper(root.right, problem, [root, ranges[1]])
        
        init_low = TreeNode(-float('inf'))
        init_high = TreeNode(float('inf'))
        problem = []
        helper(root, problem, [init_low, init_high])
        
        if len(problem) == 2: 
            problem[0][0].val, problem[1][0].val = problem[1][0].val, problem[0][0].val
            problem = []
        elif len(problem) == 1:
            if problem[0][0].val < problem[0][1].val:
                _, m = mnode(problem[0][0])
                m.val, problem[0][1].val = problem[0][1].val, m.val
            elif problem[0][0].val > problem[0][2].val:
                m, _ = mnode(problem[0][0])
                m.val, problem[0][2].val = problem[0][2].val, m.val
       
            
        