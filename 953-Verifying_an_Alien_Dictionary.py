class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        p, prev = {b: a for b, a in zip(order, string.ascii_lowercase)}, "0"
        for word in words:
            curr = "".join(p[c] for c in word)
            if curr < prev: return False
            prev = curr
        return True