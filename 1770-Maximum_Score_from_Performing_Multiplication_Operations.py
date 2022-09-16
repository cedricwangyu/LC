from functools import lru_cache
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        memory = [max(multipliers[-1] * nums[i], multipliers[-1] * nums[n-m+i]) for i in range(m)]
        for i in range(m-1, 0, -1):
            memory = [max(nums[j] * multipliers[i-1] + memory[j+1], nums[n-i+j] * multipliers[i-1] + memory[j]) for j in range(i)]
        
        return memory[0]
                