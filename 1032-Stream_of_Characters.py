class StreamChecker:

    def __init__(self, words: List[str]):
        self.dic = {}
        for w in words:
            q = self.dic
            for c in w[::-1]:
                if c not in q: q[c] = {}
                q = q[c]
            q['.'] = None
        self.stream = ""
                    

    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        q = self.dic
        for c in self.stream:
            if '.' in q: return True
            if c not in q: return False
            q = q[c]
        return '.' in q
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
