from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        c1, c2 = Counter(word1), Counter(word2)
        res = [item in c2.keys() for item in c1.keys()]
        if not all(res): return False
        L = list(c2.values())
        for v in c1.values():
            if v in L: L.remove(v)
            else: return False
        return True