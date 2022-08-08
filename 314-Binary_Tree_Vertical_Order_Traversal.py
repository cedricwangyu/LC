# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        curr_row, next_row, p, Min, Max = [(root, 0)], [], collections.defaultdict(list), 0, 0
        while len(curr_row) > 0:
            next_row.clear()
            for node, alias in curr_row:
                p[alias].append(node.val)
                if node.left: 
                    next_row.append((node.left, alias-1))
                    Min = alias - 1 if alias - 1 < Min else Min
                if node.right:
                    next_row.append((node.right, alias+1))
                    Max = alias + 1 if alias + 1 > Max else Max
            curr_row, next_row = next_row, curr_row
        result = []
        for i in range(Min, Max+1):
            if i in p: result.append(p[i])
        return result
            
                    
        
            
            