import heapq
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        p = {}
        for num in nums:
            if num in p:
                length = heapq.heappop(p[num])
                if len(p[num]) == 0:
                    del p[num]
            else:
                length = 0
            if num+1 in p:
                heapq.heappush(p[num+1], length+1)
            else:
                p[num+1] = [length+1]
        
        return all(i >= 3 for num in p for i in p[num])
                
                