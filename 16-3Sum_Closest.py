class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        p, res, dist = [], 0, 10**5
        for i in range(1, len(nums)):
            idx = bisect.bisect_left(p, nums[i])
            if len(p) > 0 and idx < len(p):
                d = p[idx] - nums[i]
                if d < dist: res, dist = target - d, d
            if len(p) > 0 and idx > 0:
                d = nums[i] - p[idx-1]
                if d < dist: res, dist = target + d, d
            for j in range(i): bisect.insort_left(p, target - nums[i] - nums[j])
        return res
