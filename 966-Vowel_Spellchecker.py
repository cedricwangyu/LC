class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        p1, p2, p3 = set(wordlist), {}, {}
        for word in wordlist:
            p2.setdefault(word.lower(), word)
            p3.setdefault("".join("-" if c in "aeiou" else c for c in word.lower()), word)
        
        for i, w in enumerate(queries):
            if w in p1: continue
            w = w.lower()
            if w in p2: 
                queries[i] = p2[w]
                continue
            w = "".join("-" if c in "aeiou" else c for c in w)
            if w in p3: queries[i] = p3[w]
            else: queries[i] = ""
        
        return queries