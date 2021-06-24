class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {}
        for a, b in edges:
            if a in g: g[a].append(b)
            else: g[a] = [b]
        if destination in g: return False
        self.visited = [False] * n
        
        @functools.lru_cache(maxsize=n)
        def dfs(curr):
            if curr not in g and curr != destination: return False
            elif curr in g:
                for nxt in g[curr]:
                    if self.visited[nxt]: return False
                    self.visited[nxt] = True
                    if not dfs(nxt): return False
                    self.visited[nxt] = False
            return True
        return dfs(source)