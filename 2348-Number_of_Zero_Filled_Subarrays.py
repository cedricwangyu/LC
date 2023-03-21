class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr, res = 0, 0
        for n in nums:
            curr, res = (curr+1, res) if n == 0 else (0, res + curr * (curr + 1) // 2)
        
        return res + curr * (curr + 1) // 2