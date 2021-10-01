class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp1, dp2 = [0] * len(text2), [0] * len(text2)
        for c1 in text1:
            for j, c2 in enumerate(text2):
                if c1 == c2: dp2[j] = dp1[j-1]+1 if j>0 else 1 
                else: dp2[j] = max(dp1[j], dp2[j-1]) if j>0 else dp1[j]
            dp1, dp2 = dp2, dp1     
        return dp1[-1]
