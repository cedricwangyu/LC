
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        List = []
        for i, row in enumerate(mat):
            row.append(0)
            p = row.index(0)
            List.append({'index': i, 'power': p})
            List.sort(key = lambda a : a['power'])
            if (len(List) > k):
                List.pop()
        
        return [item['index'] for item in List]

        