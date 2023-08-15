class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [True, True, False]
        for i in range(1, len(nums)):
            n, res = nums[i], False
            if n == nums[i-1]:
                if dp[-2] or (n == nums[i-2] and dp[-3]):
                    res = True
            if nums[i-1] == n-1 and nums[i-2] == n-2 and dp[-3]:
                res = True
            dp.append(res)
            dp.pop(0)
        
        return dp[-1]
