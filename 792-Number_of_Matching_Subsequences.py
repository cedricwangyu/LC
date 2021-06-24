class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        p = {a: [] for a in string.ascii_lowercase}
        for w in words: p[w[0]].append(w[1:])
        for c in s:
            curr, p[c] = p[c], []
            for w in curr:
                if len(w) > 0: p[w[0]].append(w[1:])
        return len(words) - sum(len(p[d]) for d in p)