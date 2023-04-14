from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(maxsize=n**2)
        def dp(i, j):
            if i == j:
                return 1
            elif i > j:
                return 0
            elif s[i] == s[j]:
                return dp(i+1, j-1) + 2
            else:
                return max(dp(i+1, j), dp(i, j-1))
            
        return dp(0, n-1)