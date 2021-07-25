class Solution:
    def findIntegers(self, n: int) -> int:
        @functools.lru_cache(maxsize=n+1)
        def fib(m):
            if m <= 0: return 1
            return fib(m-1) + fib(m-2)
        b, prev, res, breakedout = "{0:b}".format(n), 0, 0, False
        for i, curr in enumerate(b):
            d = len(b) - i
            if curr == "1":
                res += fib(d-1)
                if prev == "1":
                    breakedout = True
                    break
            prev = curr
        return res + 1 if d == 1 and not breakedout else res
