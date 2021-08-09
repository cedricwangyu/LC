class Solution:
    def numWays(self, n: int, k: int) -> int:
        s, d, t = 0, k, k
        for i in range(2, n+1):
            s, d = d, t * (k-1)
            t = s + d
        return t