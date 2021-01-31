# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.p = {}
    
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def search(node, i, j):
            if node is None: return
            if i in self.p:
                if j in self.p[i]: self.p[i][j].append(node.val)
                else: self.p[i][j] = [node.val]
            else:
                self.p[i] = {}
                self.p[i][j] = [node.val]
            search(node.left, i - 1, j - 1)
            search(node.right, i + 1, j - 1)
        
        search(root, 0, 0)
        res = []
        for x in sorted(self.p.keys()):
            new = []
            for y in sorted(self.p[x].keys(), reverse=True): new = new + sorted(self.p[x][y])
            res.append(new)
        return res