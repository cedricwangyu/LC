class Solution:
    def minCut(self, s: str) -> int:
        d, n = defaultdict(set), len(s)
        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                d[i].add(j)
                i, j = i - 1, j + 1
        for k in range(n):
            helper(k, k)
            helper(k, k + 1)
        @lru_cache(None)
        def dp(i):
            if i == -1: return 0
            return min([dp(k-1) + 1 for k in range(0, i+1) if i in d[k]])
        return dp(n-1) - 1          