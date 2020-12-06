"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         def helper(layer):
#             if len(layer) == 0: return
#             elif len(layer) == 1:
#                 pass
#             else:
#                 for i in range(1, len(layer)):
#                     layer[i-1].next = layer[i]
#             new_layer = []
#             for node in layer:
#                 if node.left: new_layer.append(node.left)
#                 if node.right: new_layer.append(node.right)
            
#             del layer
#             helper(new_layer)
        
#         if root is None: return None
#         helper([root])
#         return root
    
    def connect(self, root: 'Node') -> 'Node':
        def helper(child, left, prev):
            if child:
                if not left: 
                    left = child
                    prev = child
                    return left, prev
                prev.next = child
                prev = child
            return left, prev
        
        if root is None: return None
        left = root
        prev = None
        while(left):
            curr = left
            left = None
            while(curr):
                left, prev = helper(curr.left, left, prev)
                left, prev = helper(curr.right, left, prev)
                curr = curr.next
        
        return root
            
            
            
            
                