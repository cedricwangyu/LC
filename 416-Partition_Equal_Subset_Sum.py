class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 == 1: return False
        S = S // 2
        curr = [False] * S
        for i in range(len(nums)):
            for j in range(len(curr)-1, -1,-1):
                if curr[j]: pass
                elif j - nums[i] > -1 and curr[j - nums[i]]: curr[j] = True
                elif j - nums[i] == -1: curr[j] = True
                if i == len(nums) - 1: return curr[j]

        