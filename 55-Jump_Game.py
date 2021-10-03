class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = 0
        for i, n in enumerate(nums):
            if i > maximum: return False
            maximum = max(maximum, i+n)
            if maximum >= len(nums)-1: return True
