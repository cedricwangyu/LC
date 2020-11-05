# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         adj = {}
#         for edge in edges:
#             if edge[0] in adj: adj[edge[0]].add(edge[1])
#             else: adj[edge[0]] = {edge[1],}
#             if edge[1] in adj: adj[edge[1]].add(edge[0])
#             else: adj[edge[1]] = {edge[0],}
        
#         poped = set()
#         while len(adj) > 2:
#             new_poped = set()
#             for i in adj:
#                 adj[i].difference_update(poped)
#                 if len(adj[i]) == 1:
#                     new_poped.add(i)
            
#             for i in new_poped:
#                 del adj[i]
#             poped = new_poped
#         res = list(adj.keys())
#         print(res)
#         if len(res) > 0: return res
#         else: return [0]
                
                
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1:
                        new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves