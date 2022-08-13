from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.m = len(words)
        self.k = len(words[0])
        self.total_len = self.m * self.k
        self.counter = Counter(words)
        starts = set(word[0] for word in words)
        ends = set(word[-1] for word in words)
        res = []
        for i in range(len(s)-self.total_len+1):
            if s[i] in starts and s[i+self.total_len-1] in ends and self.counter == Counter(s[ii:ii+self.k] for ii in range(i, i+self.total_len, self.k)):
                res.append(i)
        return res
            
                
    