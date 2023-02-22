class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_done(capacity):
            load, remain = 0, days
            for w in weights:
                if w > capacity: 
                    return False
                load += w
                if load > capacity:
                    remain -= 1 
                    load = w
                if remain < 0:
                    return False
            
            return True if remain > 0 else False
        
        left, right = 0, sum(weights)
        while right - left > 1:
            mid = (left + right) // 2
            if is_done(mid):
                right = mid
            else:
                left = mid
        return right