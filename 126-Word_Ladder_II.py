class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.notseen, self.traceback, self.curr, self.res, curr, new = set(wordList), {}, [endWord], [], {beginWord}, set()
        def findnext(word):
            res = set()
            for i in range(len(word)):
                for r in string.ascii_lowercase:
                    if r == word[i]: continue
                    cand = word[:i] + r + word[i+1:]
                    if cand in self.notseen: 
                        res.add(cand)
                        if cand in self.traceback: self.traceback[cand].append(word)
                        else: self.traceback[cand] = [word]
            return res
        def gen_res():
            for w in self.traceback[self.curr[0]]:
                if w == beginWord: self.res.append([w] + self.curr)
                else: 
                    self.curr.insert(0, w)
                    gen_res()
                    self.curr.pop(0)
        while len(curr) > 0:
            for w in curr: new.update(findnext(w))
            self.notseen.difference_update(new)
            curr, new = new, curr
            new.clear()
            if endWord in curr: break
        else: return []
        gen_res()
        return self.res   
