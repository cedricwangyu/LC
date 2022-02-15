class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        p = set()
        while len(nums) > 0:
            a = nums.pop()
            if a in p: p.remove(a)
            else: p.add(a)
        return list(p)[0]