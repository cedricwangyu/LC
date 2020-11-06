import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def cal(nums, divisor):
            return sum([math.ceil(num / divisor) for num in nums])
        
        low = math.ceil(sum(nums) / threshold)
        high = max(nums)
        if cal(nums, low) <= threshold:
            return low
        while high - low > 1:
            mid = int((high + low) / 2)
            mid_res = cal(nums, mid)
            if mid_res > threshold:
                low = mid
            else:
                high = mid
        
        return high
        