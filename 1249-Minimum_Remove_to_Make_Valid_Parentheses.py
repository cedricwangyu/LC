class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p = [[], []]
        for i, c in enumerate(s):
            if c == '(': p[0].append(i)
            if c == ')':
                if len(p[0]) > 0: p[0].pop()
                else: p[1].append(i)
        
        p = sorted([*p[0], *p[1]])
        if len(p) <= 0: return s
        res = s[:p[0]]
        for i in range(1, len(p)): res += s[p[i-1] + 1: p[i]]
        res += s[p[-1]+1:]
        return res