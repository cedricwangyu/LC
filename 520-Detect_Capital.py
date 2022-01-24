class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1: return True
        first = word[0].isupper()
        last_u = word[1:].isupper()
        last_l = word[1:].islower()
        return True if (first and (last_u or last_l)) or (not first and last_l) else False
        