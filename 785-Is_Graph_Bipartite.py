class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        p, curr, new = {i: graph[i] for i in range(len(graph)) if len(graph[i]) > 0}, set(), set()
        while(len(p) > 0):
            if len(curr) <= 0: curr.add(list(p.keys())[0])
            else:
                new.clear()
                for node in curr:
                    if node not in p: return False
                    for nextnode in graph[node]: 
                        new.add(nextnode)
                        graph[nextnode].remove(node)
                    del p[node]
                curr.clear()
                curr.update(new)
        if len(curr) <= 0: return True
        else: return False