class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, curr = [nums[0]], 1
        for n in nums[1:]: res.append(res[-1]*n)
        for i in range(len(nums)-1, -1, -1):
            if i == 0: res[i] = curr
            else: res[i] = curr * res[i-1]
            curr *= nums[i]
        return res
        