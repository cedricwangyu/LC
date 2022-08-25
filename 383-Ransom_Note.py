class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        p = defaultdict(int)
        for c in ransomNote:
            p[c] -= 1
        for c in magazine:
            p[c] += 1
        
        return False if any(p[c] < 0 for c in p) else True
        