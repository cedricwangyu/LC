class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        l, r = 0, 0
        while True:
            if  r >= len(s) or s[r] == " ": s[l:r], l = reversed(s[l:r]), r + 1
            if r >= len(s): break
            r += 1