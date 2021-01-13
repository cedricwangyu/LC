class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def istrans(w1, w2):
            diff = False
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    if diff: return False
                    else: diff = True
            return True

        p, n = {}, len(beginWord)
        for w in wordList:
            diff = 0
            for i in range(n): diff += (w[i] != beginWord[i])
            if diff in p: p[diff].add(w)
            else: p[diff] = set([w])
        p[0] = set([beginWord])
        if 1 not in p: return 0
        curr, remain, cand = p[0], p[1], set()
        for i in range(1, len(wordList) + 2):
            if i in p : remain = remain.difference(curr).union(p[i])
            else: remain = remain.difference(curr)
            cand.clear()
            for wr in remain:
                for wc in curr:
                    if istrans(wr, wc):
                        cand.add(wr)
                        if wr == endWord: return i + 1
            if len(cand) <= 0: return 0 
            curr.clear()
            curr.update(cand)
            