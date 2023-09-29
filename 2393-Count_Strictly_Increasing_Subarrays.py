class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res, prev, curr = 0, nums[0], 0
        for num in nums:
            if num > prev:
                curr += 1
            else:
                res += curr * (curr + 1) // 2
                curr = 1
            prev = num
        
        return res + curr * (curr + 1) // 2