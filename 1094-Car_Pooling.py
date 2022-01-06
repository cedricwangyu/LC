class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        state = [0] * 1001
        for trip in trips:
            state[trip[1]] += trip[0]
            state[trip[2]] -= trip[0]
        
        curr = 0
        for s in state:
            curr += s
            if curr > capacity: return False
        return True
