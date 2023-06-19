class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr, res = 0, 0
        for g in gain:
            curr += g
            res = max(curr, res)
        return res