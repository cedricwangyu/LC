class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        curr = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if curr == 0:
                    curr = 1
                if curr < 0:
                    return False
            elif nums[i] < nums[i-1]:
                if curr == 0:
                    curr = -1
                if curr > 0:
                    return False
        return True