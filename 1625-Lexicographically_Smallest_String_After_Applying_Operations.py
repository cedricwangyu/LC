class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def gcd(x, y):
            if x > y: y, x = x, y
            while x > 0: x, y = y % x, x
            return y
        def find_inc(x, a):
            res = int(x)
            while res < 10: res += a
            inc = res - int(x)
            return inc
        a, b, res = gcd(10, a), gcd(len(s), b), "9"*len(s)
        for i in range(0, len(s), b):
            curr = s[i:] + s[:i]
            if b % 2 == 0: inc = [0, find_inc(curr[1], a)]
            else: inc = [find_inc(curr[0], a), find_inc(curr[1], a)]
            new_curr = ""
            curr = "".join(str((int(c) + inc[i % 2]) % 10) for i, c in enumerate(curr))
            if curr < res: res = curr
        return res
            
            
            
                