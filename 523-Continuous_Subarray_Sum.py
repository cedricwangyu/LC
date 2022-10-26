class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        earliest = {0: -1}
        nums[0] %= k
        if nums[0] not in earliest: earliest[nums[0]] = 0
        for i in range(1, len(nums)):
            nums[i] = (nums[i-1] + nums[i]) % k
            if nums[i] in earliest:
                if earliest[nums[i]] < i-1: return True
            else:
                earliest[nums[i]] = i
                
        return False