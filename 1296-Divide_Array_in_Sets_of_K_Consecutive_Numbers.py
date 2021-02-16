from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        p, n = Counter(nums), len(nums)
        if n % k != 0: return False
        K = sorted(p.keys())
        while len(p) > 0:
            for i in range(K[0], K[0] + k):
                if i in p: 
                    p[i] -= 1
                    if p[i] == 0: del p[i]
                else: return False
            while len(K) > 0 and K[0] not in p: K.pop(0)
        return True
                