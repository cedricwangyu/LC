class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        p, curr, add = {string.ascii_lowercase[i]: i for i in range(26)}, "", 0
        for c, inc in zip(s[::-1], shifts[::-1]): add, curr = add + inc, string.ascii_lowercase[(p[c] + add + inc) % 26] + curr
        return curr
