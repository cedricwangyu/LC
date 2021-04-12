class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1, c2, s = 0, 0, s.lower()
        for c in s[: len(s) // 2]:
            if c in 'aeiou': c1 += 1
        for c in s[len(s) // 2:]:
            if c in 'aeiou': c2 += 1
        return True if c1 == c2 else False
