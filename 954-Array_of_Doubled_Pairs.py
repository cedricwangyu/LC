class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=lambda x: abs(x))
        p = {}
        for n in arr:
            if n in p: 
                if p[n] == 1: del p[n] 
                else: p[n] -= 1
            else:
                if 2*n in p: p[2*n] += 1
                else: p[2*n] = 1
        return True if len(p) == 0 else False
