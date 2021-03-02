class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        p = {c: i for i, c in enumerate(keyboard)}
        prev, res = keyboard[0], 0
        for c in word:
            res += abs(p[c] - p[prev])
            prev = c
        return res