class Solution:
    def rob(self, nums: List[int]) -> int:
        yes, no = 0, 0
        for n in nums: yes, no = no+n, max(yes, no)
        return max(yes, no)
