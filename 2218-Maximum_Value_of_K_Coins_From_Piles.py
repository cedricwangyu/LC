from functools import lru_cache
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(maxsize=len(piles)*k)
        def dp(i=0, remain=k):
            if i >= len(piles) or remain == 0:
                return 0
            total, curr, res = min(remain, len(piles[i])), 0, dp(i+1, remain)
            for ii in range(total):
                curr += piles[i][ii]
                res = max(res, curr + dp(i+1, remain - ii - 1))
            return res
        
        return dp()