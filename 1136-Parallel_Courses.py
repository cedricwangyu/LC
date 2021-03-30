class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        p = {i+1: set() for i in range(n)}
        for r in relations: p[r[1]].add(r[0])
        todo, res = set(i for i in p if len(p[i]) <= 0), 0
        while len(todo) > 0:
            for i in todo: del p[i]
            for i in p: p[i].difference_update(todo)
            todo.clear()
            todo.update(i for i in p if len(p[i]) <= 0)
            res += 1
        if len(p) > 0: return -1
        else: return res