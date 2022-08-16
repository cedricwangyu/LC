class Solution:
    def firstUniqChar(self, s: str) -> int:
        p = defaultdict(int)
        seen = set()
        for i, c in enumerate(s):
            if c in seen: continue
            if c not in p: p[c] = i
            else: 
                seen.add(c)
                del p[c]
        return min(p[c] for c in p) if len(p) > 0 else -1
            