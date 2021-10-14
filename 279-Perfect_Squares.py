class Solution:
    def numSquares(self, n: int) -> int:
        p, sq = [0] * (n+1), [i**2 for i in range(1, int(math.sqrt(n))+1)]
        for i in range(1, 101):
            if i**2 > n: break
            else: p[i**2] = 1
        for i in range(1, n+1):
            if p[i] == 0: p[i] = min(p[i-ii] for ii in sq if ii < i)+1
        return p[-1]
