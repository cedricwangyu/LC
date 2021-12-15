class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        p, res = defaultdict(lambda: defaultdict(int)), 0
        for i in range(1, len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                if d not in p[j]: p[i][d] = 2
                else: p[i][d] = p[j][d] + 1
                res = max(res, p[i][d])
        return res
