class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            bisect.insort_left(res, (point[0] ** 2 + point[1] ** 2, point))
            if len(res) > k: res.pop()
        return [item[1] for item in res]
