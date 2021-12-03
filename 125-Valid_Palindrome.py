class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for ss in s:
            if ss.isalnum(): res += ss.lower()
        return res == res[::-1]
