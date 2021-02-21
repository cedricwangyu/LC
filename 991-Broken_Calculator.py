class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y <= X: return X - Y
        n = 1
        while X * 2 ** n < Y: n += 1
        diff, res = X * 2 ** n - Y, n
        for i in range(n, -1, -1):
            m = diff // (2 ** i)
            res += m
            diff = diff - m * (2 ** i)
        return res