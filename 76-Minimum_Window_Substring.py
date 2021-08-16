class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        p = collections.Counter(t)
        status, q = 0, defaultdict(int)
        for j, c in enumerate(s):
            if c in p: 
                q[c] += 1
                if q[c] == p[c]: status += 1
            if status == len(p): break
        if status < len(p): return ""
        i, status, res_count, res = 0, None, float('Inf'), ""
        while i < len(s):
            if status:
                j += 1
                if j >= len(s): break
                if s[j] in p:
                    q[s[j]] += 1
                    if s[j] == status: status = None
            else:
                if j - i + 1 < res_count: res_count, res = j - i + 1, s[i:j+1]
                if s[i] in p: 
                    q[s[i]] -= 1
                    if q[s[i]] < p[s[i]]: status = s[i]
                i += 1
        return res   
