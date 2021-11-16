class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_le(num):
            return sum(min(n, num // i) for i in range(1, m+1))
        
        lv, rv, lc, rc = 1, m*n, 1, m*n
        if k in (lc, rc): return k
        while rv-lv > 1:
            mv = (lv+rv)//2
            mc = count_le(mv)
            if mc < k: lv = mv
            else: rv = mv
        return rv
