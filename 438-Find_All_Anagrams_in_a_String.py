class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        p_count, s_count, res = collections.Counter(p), collections.Counter(s[:len(p)]), []
        for i in range(len(s)-len(p)+1):
            if s_count == p_count: res.append(i)
            s_count[s[i]] -= 1
            if s_count[s[i]] == 0: del s_count[s[i]]
            if len(p) + i >= len(s): break
            if s[len(p)+i] in s_count: s_count[s[len(p)+i]] += 1
            else: s_count[s[len(p)+i]] = 1
        return res
            