class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.curr, self.res = [], []
        def dfs(i):
            self.curr.append(i)
            if i == len(graph)-1: self.res.append(self.curr.copy())
            for j in graph[i]: dfs(j)
            self.curr.pop()
        dfs(0)
        return self.res
