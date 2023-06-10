from math import sqrt
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        r = n - index - 1
        (x1, x2) = (index, r) if index < r else (r, index)
        res = sqrt(maxSum)
        if res < x1:
            return int(res) + 1
        res = (sqrt((2 * x1 + 1) ** 2 + 4 * ((x1 + 1) * x1 + 2 * maxSum)) - (2 * x1 + 1)) / 2
        if x1 <= res < x2:
            return int(res) + 1
        res = (2 * maxSum + x1 * (x1 + 1) + x2 * (x2 + 1)) / (x1 + x2 + 1) / 2
        if res >= x2:
            return int(res) + 1
        
