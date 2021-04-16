import collections
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l, p = 0, Counter(s[:k])
        while True:
            if len(p) == 1 and p[list(p.keys())[0]] == k:
                s, l = s[:l] + s[l+k:], max(0, l - k)
                p.clear()
                p.update(Counter(s[l:l+k]))
            elif l + k + 1 <= len(s):
                p[s[l]] -= 1
                if p[s[l]] == 0: del p[s[l]]
                if p[s[l+k]]: p[s[l+k]] += 1
                else: p[s[l+k]] = 1
                l += 1
            else: return s 
