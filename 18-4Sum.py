class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        p, res = {}, set()
        for i, a in enumerate(nums):
            for j in range(i+1, len(nums)):
                s = a + nums[j]
                if s in p:
                    for l in p[s]:
                        if i not in l and j not in l: 
                            res.add(tuple(sorted([nums[i], nums[j], nums[l[0]], nums[l[1]]])))
                if target - s in p: p[target - s].append([i, j])
                else: p[target - s] = [[i, j]]
        return res
