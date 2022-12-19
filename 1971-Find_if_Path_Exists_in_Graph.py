from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = {source}
        todo = [source]
        while todo:
            u = todo.pop(0)
            for v in graph[u]:
                if v == destination:
                    return True
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
        