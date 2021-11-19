class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(s=='1' for s in bin(x ^ y))
