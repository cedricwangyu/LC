class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left_sum, right_sum, n = 0, sum(nums), len(nums)
        curr_idx, curr_val = 0, float('Inf')
        for i, num in enumerate(nums):
            left_sum += num
            right_sum -= num
            curr = abs(left_sum // (i+1) - right_sum // max(1, n-i-1))
            if curr < curr_val:
                curr_idx, curr_val = i, curr
        
        return curr_idx