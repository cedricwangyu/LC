class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dist, curr = [], [-1, -1, -1]
        for i, c in enumerate(colors):
            for i in range(3): curr[i] = curr[i] + 1 if curr[i] >= 0 else -1
            curr[c-1] = 0
            dist.append(curr.copy())
        curr = [-1, -1, -1]
        for i in range(len(colors)-1, -1, -1):
            for j in range(3): curr[j] = curr[j] + 1 if curr[j] >= 0 else -1
            curr[colors[i]-1] = 0
            for j in range(3): dist[i][j] = min(curr[j], dist[i][j]) if curr[j] >= 0 and dist[i][j] >= 0 else max(curr[j], dist[i][j])
        return [dist[i][j-1] for i, j in queries]