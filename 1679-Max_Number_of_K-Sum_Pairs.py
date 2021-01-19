class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        p, res = {}, 0
        for num in nums:
            if k - num in p:
                if p[k - num] > 1: p[k - num] -= 1
                else: del p[k - num]
                res += 1
            else:
                if num in p: p[num] += 1
                else: p[num] = 1
        return res
                
        