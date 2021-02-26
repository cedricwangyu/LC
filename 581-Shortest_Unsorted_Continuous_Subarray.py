class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp, maxbefore =  - 10 ** 6, []
        for n in nums:
            temp = max(temp, n)
            maxbefore.append(temp)
        temp, minafter = 10 ** 6, []
        for n in nums[::-1]:
            temp = min(temp, n)
            minafter.insert(0, temp)
        for i in range(len(nums)):
            if nums[i] != maxbefore[i] or nums[i] != minafter[i]: break
        left = i
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != maxbefore[i] or nums[i] != minafter[i]: break
        res = i - left + 1 if i - left > 0 else 0
        return res