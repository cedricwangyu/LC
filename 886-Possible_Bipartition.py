from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.graph = defaultdict(list)
        for u, v in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        self.labels = [-1] * (n+1)
        def bfs(u):
            self.labels[u] = 0
            todo = [(u, 0)]
            while todo:
                uu, label = todo.pop(0)
                for vv in self.graph[uu]:
                    if self.labels[vv] < 0:
                        self.labels[vv] = 1 - label
                        todo.append((vv, 1 - label))
                    elif self.labels[vv] == label:
                        return False
            return True
        for i in range(1, n+1):
            if self.labels[i] < 0 and not bfs(i):
                return False
        return True