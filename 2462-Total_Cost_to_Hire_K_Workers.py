import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        first, last = [], []
        if len(costs) > 2 * candidates:
            for _ in range(candidates):
                heapq.heappush(first, costs.pop(0))
            for _ in range(candidates):
                heapq.heappush(last, costs.pop())
        else:
            costs.sort()
            return sum(costs[:k])
        res = 0
        for _ in range(k):
            if costs:
                if first[0] <= last[0]:
                    res += heapq.heappop(first)
                    heapq.heappush(first, costs.pop(0))
                else:
                    res += heapq.heappop(last)
                    heapq.heappush(last, costs.pop())
            else:
                if last:
                    first += last
                    last.clear()
                    heapq.heapify(first)
                res += heapq.heappop(first)
        return res
            

            