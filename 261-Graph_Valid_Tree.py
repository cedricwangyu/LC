class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        p = defaultdict(set)
        for e in edges: 
            p[e[0]].add(e[1])
            p[e[1]].add(e[0])
        seen, todo = [False] * n, [0]
        while len(todo) > 0:
            ne = todo.pop(0)
            if seen[ne]: return False
            seen[ne] = True
            for nne in p[ne]:
                p[nne].remove(ne)
                todo.append(nne)
        return True if all(seen) else False
