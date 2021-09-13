class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        p = collections.Counter(text)
        for c in "balon": 
            if c not in p: return 0
        return min(p['b'], p['a'], p['l']//2, p['o']//2, p['n'])
