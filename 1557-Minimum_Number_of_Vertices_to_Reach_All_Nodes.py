class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set(i for i in range(n))
        for _, b in edges:
            if b in res:
                res.remove(b)
        return list(res)