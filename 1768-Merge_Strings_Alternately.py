class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, res = min(len(word1), len(word2)), ""
        for i in range(n):
            res += word1[i] + word2[i]
        return res + word1[n:] if len(word1) > n else res + word2[n:]