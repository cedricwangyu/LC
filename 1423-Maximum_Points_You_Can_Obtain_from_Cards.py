class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints): return sum(cardPoints)
        s = sum(cardPoints[-k:])
        res = s
        for i in range(k):
            s += cardPoints[i] - cardPoints[-k+i]
            res = max(res, s)
        return res
