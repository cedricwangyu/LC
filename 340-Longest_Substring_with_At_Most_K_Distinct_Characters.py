class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        elif len(s) <= k: return len(s)
        start, p, res = 0, {}, 0
        for end, c in enumerate(s):
            if c in p: p[c] += 1
            else: p[c] = 1
            while len(p) > k:
                if p[s[start]] == 1: del p[s[start]]
                else: p[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        
        return res
                