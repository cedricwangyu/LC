class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l, r = 1, max(ribbons)
        if sum(ribbons) < k: return 0
        if sum(rib == r for rib in ribbons) >= k: return r
        while r-l>1:
            m = (l+r)//2
            n = sum(rib // m for rib in ribbons)
            if n < k: r = m
            else: l = m
        return l
        
