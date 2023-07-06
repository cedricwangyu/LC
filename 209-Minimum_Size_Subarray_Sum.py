class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, res, curr = 0, 0, len(nums)+1, 0
        while right <= len(nums):
            if curr < target:
                if right < len(nums):
                    curr += nums[right]
                else:
                    break
                right += 1
            else:
                res = min(res, right - left)
                curr -= nums[left]
                left += 1
        return res if res <= len(nums) else 0
                