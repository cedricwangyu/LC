import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(s):
            if s == '': return 0
            c = Counter(s)
            for char in c.keys():
                if c[char] < k: break
            else: return len(s)
            id = s.index(char)
            return max(helper(s[:id]), helper(s[id+1:]))
        
        return helper(s)
            