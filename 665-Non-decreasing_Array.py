class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        record = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if record is None: record = i
                else: return False
        if record is None or record in (0, len(nums) - 2) or nums[record - 1] <= nums[record + 1] or nums[record] <= nums[record + 2]: return True
        else: return False
