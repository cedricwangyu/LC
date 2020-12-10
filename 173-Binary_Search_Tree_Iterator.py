# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.path = [root]
        self.rightmost = root
        self.node = root
        self.begin = True
        while self.node.left:
            self.path.append(self.node.left)
            self.node = self.node.left
        while self.rightmost.right: self.rightmost = self.rightmost.right
        
    def righthelper(self):
        self.path.append(self.node.right)
        self.node = self.node.right
        while (self.node.left):
            self.path.append(self.node.left)
            self.node = self.node.left
        
    def next(self) -> int:
        if self.begin:
            self.begin = False
            return self.node.val
        v = self.node.val
        
        if self.node.right is not None: self.righthelper()
        else:
            while(self.node.val <= v):
                self.path.pop()
                self.node = self.path[-1]
        return self.node.val
            
    def hasNext(self) -> bool:
        if self.node.val < self.rightmost.val or self.begin: return True
        else: return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()