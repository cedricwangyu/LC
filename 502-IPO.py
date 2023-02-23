import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        info, res, q, idx = sorted(zip(capital, profits)), w, [], 0
        for t in range(k):
            while idx < len(info) and info[idx][0] <= res:
                heapq.heappush(q, -info[idx][1])
                idx += 1
            if q:
                res += -heapq.heappop(q)
            else:
                break