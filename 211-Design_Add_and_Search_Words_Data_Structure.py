class WordDictionary:

    def __init__(self):
        self.p = {}

    def addWord(self, word: str) -> None:
        d = self.p
        for c in word:
            if c not in d: d[c] = {}
            d = d[c]
        d["#"] = {}
        
    def search(self, word: str) -> bool:
        def search_dict(d, w):
            if len(w) == 0: 
                return "#" in d
            else:
                c = w[0]
                if c == ".": return any(search_dict(d[k], w[1:]) for k in d)
                elif c in d: return search_dict(d[c], w[1:])
                else: return False
        return search_dict(self.p, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)