class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        def twoSumSmaller(start, ttarget):
            l, r, res = start, len(nums)-1, 0
            while l<r:
                if nums[l] + nums[r] >= ttarget: r -= 1
                else: res, l = res + r - l, l + 1
            return res
        ans = 0
        for i in range(len(nums)-2): ans += twoSumSmaller(i+1, target-nums[i])
        return ans
