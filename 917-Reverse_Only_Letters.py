class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ss, j = "", len(s) - 1
        for i in range(len(s)):
            if s[i].isalpha():
                while not s[j].isalpha(): j -= 1
                ss, j = ss+s[j], j-1
            else: ss += s[i]
        return ss