class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def if_can_be_done(k):
            amount = 0
            for p in piles: amount += (p // k + int(p % k > 0))
            return amount <= h
        
        l, r = 1, max(piles)
        if if_can_be_done(l): return 1
        while r - l > 1:
            m = (r+l) // 2
            if if_can_be_done(m): r = m
            else: l = m
        
        return r
