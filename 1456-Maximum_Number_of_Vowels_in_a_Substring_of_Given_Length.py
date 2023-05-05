class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        curr = 0
        for c in s[:k]:
            if c in vowels:
                curr += 1
        res = curr
        for i, c in enumerate(s[k:]):
            if c in vowels:
                curr += 1
            if s[i] in vowels:
                curr -= 1
            res = max(res, curr)
        return res