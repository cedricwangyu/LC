class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        state, res = [False] * len(nums), 0
        for i in range(len(nums)):
            if state[i]: continue
            state[i], ii, curr = True, nums[i], 1
            while ii != i: ii, curr, state[ii] = nums[ii], curr + 1, True
            res = max(res, curr)
        return res
