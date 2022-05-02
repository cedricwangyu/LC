class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        idx, n = 0, len(nums)
        for _ in range(n):
            if nums[idx] % 2 == 1:nums.append(nums.pop(idx))
            else: idx += 1
        return nums