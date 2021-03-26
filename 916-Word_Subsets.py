class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        p, res = {}, []
        for word in B:
            c = collections.Counter(word)
            for k in c.keys():
                if k in p: p[k] = max(p[k], c[k])
                else: p[k] = c[k]
        for word in A:
            c, cb = collections.Counter(word), True
            for k in p.keys():
                if k not in c or p[k] > c[k]: 
                    cb = False
                    break
            if cb: res.append(word)
        return res