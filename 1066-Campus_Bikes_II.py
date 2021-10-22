class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)
        
        @cache
        def fn(i, mask):
            if i == n: return 0 
            ans = inf 
            for j in range(m): 
                if not mask & (1<<j): 
                    ans = min(ans, abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]) + fn(i+1, mask ^ (1<<j)))
            return ans 
        
        return fn(0, 0)
