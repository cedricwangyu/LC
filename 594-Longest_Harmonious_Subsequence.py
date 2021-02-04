from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if len(counter) <= 1: return 0
        K, res = sorted(counter.keys()), 0
        for i in range(1, len(K)):
            if K[i] == K[i-1] + 1: res = max(res, counter[K[i]] + counter[K[i-1]])
        
        return res