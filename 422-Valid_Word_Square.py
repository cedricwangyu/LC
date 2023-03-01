class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n, m = len(words), max(len(word) for word in words)
        if n != m: return False
        for i in range(n-1):
            for j in range(i+1, m):
                if j >= len(words[i]) and i >= len(words[j]):
                    continue
                elif j < len(words[i]) and i < len(words[j]):
                    if words[i][j] != words[j][i]:
                        return False
                else:
                    return False
        return True