class Solution:
    def numTilings(self, n: int) -> int:
        n01, n11, n10, n21, n20 = 0, 0, 0, 1, 0
        for m in range(n): n01, n11, n10, n21, n20 = n11, n21, n20, n21 + 2 * n20 + n11, n11 + n20
        return n21 % 1000000007