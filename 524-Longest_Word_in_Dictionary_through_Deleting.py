class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def fit(word):
            i = 0
            for c in s:
                if c == word[i]: i += 1
                if i >= len(word): return True
            return False
        
        res = ""
        for word in d:
            if len(word) < len(res) or (len(word) == len(res) and word > res): continue
            if fit(word): res = word
        return res