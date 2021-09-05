class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1: return "".join(sorted(s))
        else:
            res = s
            for i in range(1,len(s)):
                if s[i:] + s[:i] < res: res = s[i:] + s[:i]
            return res