class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res, p = 0, []
        for w in words:
            ws = set(w)
            for s in p:
                if len(s[0].intersection(ws)) == 0: res = max(res, len(w) * s[1])
            p.append((ws, len(w)))
        return res
