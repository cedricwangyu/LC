class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = (high - low + 1)
        return res // 2 if res % 2 == 0 else res // 2 + int(low % 2 == 1)