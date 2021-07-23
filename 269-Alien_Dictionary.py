class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.p, self.contra = set(), False
        def grouping(iterable, n):
            res = ""
            for w, g in itertools.groupby([w if len(w) > n else w + "." for w in iterable ], key=lambda x: x[n]):
                if w in res or (w == "." and len(res) > 0): self.contra = True
                res += w
                if not w == ".": grouping(g, n+1)
            if len(res) > 0: self.p.add(res)
        grouping(words, 0)
        if self.contra: return ""
        if '.' in self.p: self.p.remove('.')
        self.p, self.res = [w[1:] if w[0] == '.' else w for w in self.p], ""
        while len(self.p) > 0:
            cand = {w[0] for w in self.p}
            for c in cand:
                if not any(c in w[1:] for w in self.p):
                    self.res, i = self.res + c, 0
                    while i < len(self.p):
                        if self.p[i][0] == c:
                            if len(self.p[i]) == 1: 
                                self.p.pop(i)
                                continue
                            else: self.p[i] = self.p[i][1:]
                        i += 1
                    break
            else: return ""
        return self.res 
