class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        p, initials = {}, ""
        for name in ideas:
            if name[:1] in p:
                p[name[:1]].add(name[1:])
            else:
                p[name[:1]] = {name[1:],}
                initials += name[:1]
        if len(initials) < 2: return 0
        res = 0
        for i in range(len(initials)-1):
            for j in range(i+1, len(initials)):
                inter_num = len(p[initials[i]].intersection(p[initials[j]]))
                res += 2 * (len(p[initials[i]]) - inter_num) * (len(p[initials[j]]) - inter_num)
        return res