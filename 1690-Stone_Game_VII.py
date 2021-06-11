class Solution:
    def stoneGameVII(self, A):
        CSum = [0] + list(accumulate(A))
        @lru_cache(2000)
        def dp(i, j):
            if i > j: return 0
            sm = CSum[j + 1] - CSum[i]
            return sm - min(A[i] + dp(i+1, j), A[j] + dp(i, j-1))
        return dp(0, len(A) - 1)
