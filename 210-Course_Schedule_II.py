class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        p, res = {i: [set(), set()] for i in range(numCourses)}, []
        for c1, c2 in prerequisites:
            p[c1][0].add(c2)
            p[c2][1].add(c1)
        while len(p) > 0:
            for i in p:
                if len(p[i][0]) == 0:
                    res.append(i)
                    for ni in p[i][1]:
                        if ni in p: p[ni][0].remove(i)
                    del p[i]
                    break
            else: return []
        return res
