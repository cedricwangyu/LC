class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr, tmp_max, tmp_min, max_inc, max_dec, maxi = 0, 0, 0, -float('Inf'), float('Inf'), -float('Inf')
        for num in nums:
            curr += num
            if num > maxi: maxi = num
            max_inc = max(max_inc, curr - tmp_min)
            max_dec = min(max_dec, curr - tmp_max)
            if curr > tmp_max: tmp_max = curr
            if curr < tmp_min: tmp_min = curr
        
        return max(max_inc, curr - max_dec) if max_inc > 0 else maxi