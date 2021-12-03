class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.p = {}
        for w in wordDict:
            q = self.p
            for c in w:
                if c not in q: q[c] = {}
                q = q[c]
            q["."] = None
        self.res = []
        def read(i, q, curr_w, curr_s):
            if i >= len(s): 
                if "." in q: self.res.append(curr_s + " " + curr_w)
                return
            if "." in q: read(i, self.p, "", curr_s + " " + curr_w)
            if s[i] in q: read(i+1, q[s[i]], curr_w + s[i], curr_s)
        
        read(0, self.p, "", "")
        return [item[1:] for item in self.res]
            
