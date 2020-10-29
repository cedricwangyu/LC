"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        def helper(root, biroot):
            if root.children:
                biroot.left = TreeNode(root.children[0].val)
                currnode = biroot.left
                helper(root.children[0], currnode)
            else:
                return
            
            for cd in root.children[1:]:
                currnode.right = TreeNode(cd.val)
                currnode = currnode.right
                helper(cd, currnode)
        if root:
            biroot = TreeNode(root.val)
            helper(root, biroot)
            return biroot
        else:
            return

                
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        def helper(root, biroot):
            if biroot.left:
                curr = biroot.left
                root.children = [Node(curr.val)]
                helper(root.children[0], curr)
                while curr.right is not None:
                    curr = curr.right
                    root.children.append(Node(curr.val))
                    helper(root.children[-1], curr)
            else:
                root.children = []
        if data:
            root = Node(data.val)
            helper(root, data)
            return root
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))