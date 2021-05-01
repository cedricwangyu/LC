class WordFilter:
    def __init__(self, words: List[str]):
        self.p = {}
        for i, w in enumerate(words):
            if w[0] + w[-1] in self.p: self.p[w[0]+w[-1]].insert(0, (w, i))
            else: self.p[w[0]+w[-1]] = [(w, i)]
        
    def f(self, prefix: str, suffix: str) -> int:
        if prefix[0]+suffix[-1] in self.p:
            for w, i in self.p[prefix[0]+suffix[-1]]:
                if len(prefix) <= len(w) and len(suffix) <= len(w) and w[:len(prefix)] == prefix and w[-len(suffix):] == suffix: return i    
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)