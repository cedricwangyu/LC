class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        if k==0: return sum(sweetness)
        def is_doable(m):
            curr, p = 0, 0
            for s in sweetness:
                curr += s
                if curr >= m: curr, p = 0, p+1
                if p > k: return True
            return False
        
        l, r = 1, sum(sweetness) // (k+1)
        if is_doable(r): return r
        while r-l > 1:
            m = (l+r)//2
            if is_doable(m): l=m
            else: r=m
        return l
