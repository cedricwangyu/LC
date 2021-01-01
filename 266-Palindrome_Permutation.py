class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        p = set()
        for c in s:
            if c in p: p.remove(c)
            else: p.add(c)
        if len(p) < 2: return True
        else: return False