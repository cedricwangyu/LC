class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        p = set()
        for n in nums:
            if n in p: p.remove(n)
            else: p.add(n)
        return p
