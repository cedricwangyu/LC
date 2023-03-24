class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1
        p = defaultdict(set)
        for a, b in connections:
            p[a].add(b)
            p[b].add(a)
        
        todo, seen, cluster_count, I = [], set(), 0, 0
        while len(seen) < n:
            while I in seen:
                I += 1
            todo.append(I)
            seen.add(I)
            while todo:
                i = todo.pop(0)
                for ni in p[i]:
                    if ni not in seen:
                        todo.append(ni)
                        seen.add(ni)
            cluster_count += 1

        return cluster_count - 1