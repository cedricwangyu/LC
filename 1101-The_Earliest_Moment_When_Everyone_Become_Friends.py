class Union:
    def __init__(self, data):
        self.data = data
        
    def find(self, i):
        if i != self.data[i]: self.data[i] = self.find(self.data[i])
        return self.data[i]
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj: self.data[pi] = pj
    def all_connected(self):
        p = self.find(0)
        return all(self.find(c) == p for c in self.data)

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if n-1 > len(logs): return -1
        u = Union([i for i in range(n)])
        logs.sort(key=lambda x: x[0])
        for t, i, j in logs[:(n-1)]: u.union(i, j)
        
        if u.all_connected(): return t
        for t, i, j in logs[(n-1):]:
            u.union(i, j)
            if u.all_connected(): return t
        return -1
            
            
        