class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(i, j):
            if i < 0: return True if j < 0 or (j % 2 == 1 and all(p[jj] == "*" for jj in range(j + 1) if jj % 2 == 1)) else False
            if j < 0: return False
            if p[j] in ('.', s[i]) and helper(i - 1, j - 1): return True 
            if p[j] == "*" and p[j - 1] in ('.', s[i]) and helper(i - 1, j): return True
            if p[j] == "*" and helper(i, j - 2): return True
            return False  
        return helper(len(s) - 1, len(p) - 1)    


# class Solution(object):
#     def isMatch(self, text, pattern):
#         dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

#         dp[-1][-1] = True
#         for i in range(len(text), -1, -1):
#             for j in range(len(pattern) - 1, -1, -1):
#                 first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                 if j+1 < len(pattern) and pattern[j+1] == '*':
#                     dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
#                 else:
#                     dp[i][j] = first_match and dp[i+1][j+1]

#         return dp[0][0]