class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        temp, p = [], {}
        for s in paths:
            temp.clear()
            temp += s.split(" ")
            for c in temp[1:]:
                a, b = c.split('(')
                b = b[:-1]
                if b in p: p[b].append(temp[0]+'/'+a)
                else: p[b] = [temp[0]+'/'+a]
        return [p[c] for c in p if len(p[c]) > 1]
