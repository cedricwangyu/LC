class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r, s = 1, len(s), '0' + s + '0'
        while l < r:
            if s[l] == s[r]: l, r = l+1, r-1
            elif r == l+1 or s[l:r] == s[r-1:l-1:-1] or s[l+1:r+1] == s[r:l:-1]: return True
            else: return False
            
        return True
        