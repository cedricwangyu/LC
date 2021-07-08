class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        return "".join([w + " " for w in l[::-1] if len(w) > 0])[:-1]