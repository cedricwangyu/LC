class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        p, res = [{}], 0
        for i in range(1, len(nums)):
            d = {}
            for j in range(0, i):
                diff = nums[j] - nums[i]
                if diff in p[j]: 
                    if diff in d: d[diff][0], d[diff][1], res = d[diff][0] + 1, d[diff][1] + p[j][diff][0] + p[j][diff][1], res + p[j][diff][0] + p[j][diff][1]
                    else: d[diff], res = [1, p[j][diff][0] + p[j][diff][1]], res + p[j][diff][0] + p[j][diff][1]
                else: 
                    if diff in d: d[diff][0] += 1
                    else: d[diff] = [1, 0]
            p.append(d)
        return res
