import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target) - 1
        l = len(nums) - 1 if l == len(nums) else l
        l = l if nums[l] == target else -1
        r = r if nums[r] == target else -1
        return [l, r]