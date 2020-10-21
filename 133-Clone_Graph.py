class Solution:
    def __init__(self):
        self.passed = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        curr_node = Node(node.val, [])
        self.passed[curr_node.val] = curr_node
        for n in node.neighbors:
            if n.val not in self.passed:
                self.cloneGraph(n)
            
            curr_node.neighbors.append(self.passed[n.val])
        
        return curr_node
