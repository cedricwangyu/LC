class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1 = p2 = None
        res = len(words)
        for i, word in enumerate(words):
            if word == word1: p1 = i
            elif word == word2: p2 = i
            if p1 is not None and p2 is not None: res = min(res, abs(p1 - p2))
        
        return res
        