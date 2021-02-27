class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        def modulo(D, d):
            res = 0
            while D >= d:
                D -= d
                res += 1
            return res, D
        D = [int(i) for i in str(abs(dividend))]
        res, r = 0, 0
        for d in D:
            res = res + res + res + res + res + res + res + res + res + res
            r = r + r + r + r + r + r + r + r + r + r + d
            res_add, r = modulo(r, abs(divisor))
            res += res_add
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0): return min(res, MAX)
        else: return max(-res, MIN)