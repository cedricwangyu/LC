import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        for i in range(k):
            heapq.heappush(piles, heapq.heappop(piles) // 2)
        
        return -sum(piles)