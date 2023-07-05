class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, left, right, zero_ind = 0, 0, 0, -1
        while right < len(nums):
            if nums[right] == 0:
                res = max(res, right - left - 1)
                # print(left, zero_ind, right, res, '->', end=' ')
                if zero_ind < 0:
                    zero_ind = right
                else:
                    left = zero_ind + 1
                    zero_ind = right
                # print(left, zero_ind, right, res)
            right += 1
        # print(left, zero_ind, right, res)
        res = max(res, right - left - 1)
        return res
                
                