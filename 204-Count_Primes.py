class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        p = [False, False] + [True] * (n - 2)
        def brush(i):
            m = 2
            while m * i < len(p): p[m*i], m = False, m+1
        for i in range(2, len(p)):
            if p[i]: brush(i)
        return sum(p)