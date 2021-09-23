class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        alpha = string.ascii_lowercase
        p = {c: i for i, c in enumerate(alpha)}
        for i, c in enumerate(palindrome):
            if len(palindrome) % 2 == 1 and i == len(palindrome) // 2: continue
            elif p[c] > 0: return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b" if len(palindrome) > 1 else ""
