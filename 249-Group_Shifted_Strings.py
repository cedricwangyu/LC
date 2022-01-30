class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        p = {string.ascii_lowercase[i]: i for i in range(26)}
        def pattern(s):
            diff = p[s[0]]
            return "".join(string.ascii_lowercase[(p[c] - diff) % 26] for c in s)
        
        q = defaultdict(list)
        for s in strings: q[pattern(s)].append(s)
        return [q[n] for n in q]
            
            