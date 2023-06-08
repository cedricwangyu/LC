from bisect import bisect_right, bisect_left
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target, lo=left)
        return right - left > len(nums) // 2
        