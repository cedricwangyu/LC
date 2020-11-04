class Solution:
    def maxPower(self, s: str) -> int:
        curr_max  = 1
        hist_max = 0
        if len(s) <= 1: return len(s)
        for i in range(1,len(s)):
            if s[i] == s[i - 1]: curr_max += 1
            else:
                curr_max = 1
            hist_max = max(hist_max, curr_max)
                
        return hist_max