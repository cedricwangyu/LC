class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heappop(stones)
            s2 = heappop(stones)
            if s1 == s2: continue
            else: heappush(stones, -abs(s1-s2))
        
        return -stones[0] if len(stones) == 1 else 0