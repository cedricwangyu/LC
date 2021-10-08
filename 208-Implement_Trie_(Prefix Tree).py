class Trie:

    def __init__(self):
        self.p = {}

    def insert(self, word: str) -> None:
        if word == "": 
            self.p[""] = None
            return
        if word[0] in self.p: self.p[word[0]].insert(word[1:])
        else:
            self.p[word[0]] = Trie()
            self.p[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if word == "":
            if "" in self.p: return True
            else: return False
        if word[0] in self.p: return self.p[word[0]].search(word[1:])
        else: return False

    def startsWith(self, prefix: str) -> bool:
        if prefix == "": return True
        if prefix[0] in self.p: return self.p[prefix[0]].startsWith(prefix[1:])
        else: return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
