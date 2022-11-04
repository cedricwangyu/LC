class Solution:
    def reverseVowels(self, s: str) -> str:
        inds, chars = [], []
        for i, c in enumerate(s):
            if c in "aeiouAEIOU":
                inds.append(i)
                chars.append(c)
        s = list(s)
        for i, c in zip(inds, chars[::-1]):
            s[i] = c
            
        return "".join(s)