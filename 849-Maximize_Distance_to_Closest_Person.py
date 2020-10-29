class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = -1
        last = None
        for i in range(len(seats)):
            if seats[i] == 1:
                if last is None:
                    dist = i
                else:
                    dist = max(dist, int((i - last) / 2))
                
                last = i
        
        dist = max(dist, i - last)
        return dist