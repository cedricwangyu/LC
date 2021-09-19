class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        dp = [0 for j in range(N)] 
        for i in range(M - 1, -1, -1):
            prev = 1
            for j in range(N - 1, -1, -1):
                old_dpj = dp[j]
                if s[i] == t[j]: dp[j] += prev
                prev = old_dpj
        return dp[0]
