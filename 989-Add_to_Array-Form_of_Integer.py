class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = 0
        for n in num:
            res = 10 * res + n
        return [int(c) for c in str(res + k)]