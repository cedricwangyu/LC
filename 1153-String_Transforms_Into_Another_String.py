class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        p1, p2, i = {}, {}, 0
        for c1, c2 in zip(str1, str2):
            if c1 not in p1 and c2 not in p2: p1[c1], p2[c2], i = string.ascii_lowercase[i], string.ascii_lowercase[i], i+1
            elif c1 not in p1 and c2 in p2: p1[c1] = p2[c2]
            elif c1 in p1 and c2 in p2 and p1[c1] == p2[c2]: pass
            else: return False
        return False if i == 26 and str1 != str2 else True
