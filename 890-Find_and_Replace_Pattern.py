class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        i, key_p, key, p, res = 0, "", "", {}, []
        for c in pattern:
            if c not in p: 
                p[c] = string.ascii_lowercase[i]
                i += 1
            key_p += p[c]
        for w in words:
            p.clear()
            i, key = 0, ""
            for c in w:
                if c not in p:
                    p[c] = string.ascii_lowercase[i]
                    i += 1
                key += p[c]
            if key == key_p: res.append(w)
        return res             