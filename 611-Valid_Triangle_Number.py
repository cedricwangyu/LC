class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            j, k = i+1, i+2
            while k < len(nums):
                if nums[i] + nums[j] > nums[k]: res, k = res+k-j, k+1
                else: 
                    j += 1
                    if j == k: k += 1
        return res
