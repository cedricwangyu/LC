class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        todo = sorted([a-b for a, b in zip(capacity, rocks)], reverse=True)
        res = 0
        while len(todo) > 0 and additionalRocks > 0:
            if todo[-1] <= additionalRocks:
                additionalRocks -= todo.pop()
                res += 1
            else:
                return res
                
        return res