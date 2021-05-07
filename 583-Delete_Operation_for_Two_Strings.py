class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        p = [[0] * len(word1) for _ in range(len(word2))]
        p[0][0] = int(word1[0] == word2[0])
        for i in range(1, len(word2)): p[i][0] = int(word1[0] == word2[i] or p[i-1][0])
        for j in range(1, len(word1)): p[0][j] = int(word1[j] == word2[0] or p[0][j-1])
        for i in range(1, len(word2)):
            for j in range(1, len(word1)): p[i][j] = max(p[i-1][j], p[i][j-1], p[i-1][j-1] + int(word1[j] == word2[i]))
        return len(word1) + len(word2) - 2 * p[-1][-1]