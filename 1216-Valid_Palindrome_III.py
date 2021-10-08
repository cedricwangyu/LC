class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @functools.lru_cache(maxsize=len(s)**2)
        def helper(i, j):
            if i >= j: return 0
            if s[i] == s[j]:
                if j == i+1: return 0
                return min([helper(i+1, j-1), helper(i+1, j)+1, helper(i, j-1)+1])
            else:
                return min([helper(i+1, j), helper(i, j-1)])+1
        return helper(0, len(s)-1) <= k
