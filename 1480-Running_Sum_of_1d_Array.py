class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res, s = [], 0
        for n in nums:
            s += n
            res.append(s)
        return res
