class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        if width > height: m, n = width, height
        else: m, n = height, width
        mn, nn, mr, nr = m // sideLength, n // sideLength, m % sideLength, n % sideLength
        x, y, z = nr * mr, (sideLength - mr) * nr, (sideLength - nr) * mr
        res = mn * nn * maxOnes + (mn + nn + 1) * min(x, maxOnes)
        u = max(maxOnes - x, 0)
        res += mn * min(y, u)
        res += nn * min(max(u - y, 0), z)
        return res
        
