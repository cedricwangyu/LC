# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:

#     def serialize(self, root: TreeNode) -> str:
#         """Encodes a tree to a single string.
#         """
#         nodes = [root]
#         level = 0
#         while(any([item is not None for item in nodes[2**level - 1: 2**(level + 1) - 1]])):
#             new = []
#             for node in nodes[2**level - 1: 2**(level + 1) - 1]:
#                 if node is None:
#                     new.append(None)
#                     new.append(None)
#                 else:
#                     new.append(node.left)
#                     new.append(node.right)
#             if all([item is None for item in new]):
#                 new = []
#             nodes = nodes + new
#             level += 1
#         #print([node.val for node in nodes])
#         res = [str(-1)+',' if item is None else str(item.val)+',' for item in nodes]
#         #print(res)
#         print(''.join(res)[:-1])
#         return ''.join(res)[:-1]


        

#     def deserialize(self, data: str) -> TreeNode:
#         """Decodes your encoded data to tree.
#         """
#         vals = data.split(',')
#         vals = [int(val) if val != '-1' else None for val in vals]
#         print(vals)
#         level = 0
#         nodes = []
#         for val in vals:
#             if val is None:
#                 nodes.append(None)
#             else:
#                 node = TreeNode()
#                 node.val = val
#                 nodes.append(node)
#         #print(nodes)
#         for i, node in enumerate(nodes):
#             try: 
#                 node.left = nodes[2 * i + 1] 
#             except: 
#                 pass
#             try: 
#                 node.right = nodes[2 * i + 2] 
#             except: 
#                 pass
                
#         return nodes[0]
                
            

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        print(' '.join(map(str, postorder(root))))
        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        def helper(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
        
        data = [int(x) for x in data.split(' ') if x]
        return helper()

