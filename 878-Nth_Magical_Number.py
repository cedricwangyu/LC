class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            if x == y: return x
            elif x < y: x, y = y, x
            prod = x * y
            while x % y > 0: x, y = y, x % y
            return prod // y
        
        g = gcd(a, b)
        m = g // a + g // b - 1
        res = g * (n // m)
        n = n % m
        l1, l2, curr = a, b, 0
        for _ in range(n):
            if l1 > l2: curr, l2 = l2, l2 + b
            else: curr, l1 = l1, l1 + a
        return (res + curr) % 1000000007