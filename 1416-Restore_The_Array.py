from functools import lru_cache
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n-1, -1, -1):
            if s[i] != '0':
                for j in range(i+1, n+1):
                    if j == n or s[j] != '0':
                        if int(s[i:j]) <= k:
                            dp[i] += dp[j]
                        else:
                            break
        
        return dp[0] % (10 ** 9 + 7)