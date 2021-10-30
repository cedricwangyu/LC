class Solution:
    def longestDupSubstring(self, s: str) -> str:
        self.p = set()
        def is_duplicate(l):
            self.p.clear()
            for i in range(len(s)-l+1):
                if s[i:i+l] in self.p: return s[i:i+l]
                else: self.p.add(s[i:i+l])
            return ""
        L, R, L_res = 1, len(s)-1, is_duplicate(1)
        if len(is_duplicate(R))>0: return s[:len(s)-1]
        if len(L_res) == 0: return ""
        while R-L >1:
            M = (R+L)//2
            res = is_duplicate(M)
            if len(res) > 0: L, L_res = M, res
            else: R = M
        return L_res
