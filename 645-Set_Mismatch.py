import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        p = set(i + 1 for i in range(len(nums)))
        res = []
        for i in nums:
            if i in p: p.remove(i)
            else: res.append(i)
        res.append(list(p)[0])
        return res