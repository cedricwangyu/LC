class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s): return 0
        c = collections.Counter(s[:k])
        res = 1 if len(c) == k else 0
        for i in range(k, len(s)):
            if s[i] in c: c[s[i]] += 1
            else: c[s[i]] = 1
            c[s[i-k]] -= 1
            if c[s[i-k]] == 0: del c[s[i-k]]
            if len(c) == k: res += 1
        return res
            
            