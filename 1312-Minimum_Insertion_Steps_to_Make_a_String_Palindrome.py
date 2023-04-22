from functools import lru_cache
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        @lru_cache(maxsize=n**2)
        def dp(i=0, j=n-1):
            if i > j:
                return 0
            if s[i] == s[j]:
                return dp(i+1, j-1)
            else:
                return 1 + min(dp(i, j-1), dp(i+1, j))
        
        return dp()
            