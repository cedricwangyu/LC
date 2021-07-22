class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        p = [-1]
        p.extend(max(p[i-1], nums[i-1]) for i in range(1, len(nums)+1))
        p.pop(0)
        curr, res = 10 ** 6, 0
        for i in range(len(nums)-1, -1, -1):
            if curr >= p[i]: res = i+1 
            curr = min(curr, nums[i])
        return res
