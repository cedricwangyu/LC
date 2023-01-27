class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words, res = set(words), []
        for word in words:
            n = len(word)
            dp = [True] + [False] * n
            for i in range(1, n+1):
                for j in range(i):
                    # print(dp[j], word[j:i])
                    if dp[j] and (j > 0 or i < n) and word[j:i] in words:
                        dp[i] = True
                        break
            # print(word, dp)
            if dp[-1]:
                res.append(word)
        return res