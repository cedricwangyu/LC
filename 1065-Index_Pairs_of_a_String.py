class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        p, res = defaultdict(list), []
        for word in words:
            p[word[0]].append(word)
        for c in p:
            p[c].sort()
        
        for i, c in enumerate(text):
            if c in p:
                for w in p[c]:
                    if i + len(w) <= len(text) and text[i:i+len(w)] == w:
                        res.append([i, i+len(w)-1])
        
        return res