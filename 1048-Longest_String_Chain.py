class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        p, temp, res = {}, set(), 1
        for w in words:
            if len(w) in p: p[len(w)].append(w)
            else: p[len(w)] =  [w]
        p = list(p.values())
        p.sort(key=lambda x: len(x[0]))
        for i in range(len(p[0])): p[0][i] = [p[0][i], 1]
        for i in range(1, len(p)):
            for j, w in enumerate(p[i]):
                temp.clear()
                temp.update(w[:k] + w[k+1:] for k in range(len(w)))
                p[i][j] = [p[i][j], 1]
                for s in p[i-1]:
                    if s[0] in temp:
                        p[i][j][1] = max(p[i][j][1], s[1] + 1)
                        res = max(res, s[1] + 1)
            i += 1
        return res