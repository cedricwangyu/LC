from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        p = defaultdict(int)
        total = 0
        res = []
        for n in changed:
            if n in p and p[n] > 0:
                p[n] -= 1
                total -= 1
            else:
                res.append(n)
                p[2*n] += 1
                total += 1
        
        return res if total == 0 else []