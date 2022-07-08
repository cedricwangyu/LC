class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @functools.lru_cache(maxsize=m*n*(target+3))
        def dp(house_id, color_id, remain_group):
            res, curr_color = [float('Inf'), float('Inf')], houses[house_id]-1
            if (curr_color >= 0 and color_id != curr_color) or remain_group > target: 
                return res
            curr_cost = cost[house_id][color_id] if curr_color < 0 else 0
            if house_id == 0: 
                return (float("Inf"), curr_cost) if remain_group == target else res
            
            for color in range(n):
                idx = int(color_id != color)
                res[idx] = min(res[idx], curr_cost + dp(house_id-1, color, remain_group+1)[1], curr_cost + dp(house_id-1, color, remain_group)[0])
            return res
        
        res = min(min(dp(m-1, color, 1)[1], dp(m-1, color, 0)[0]) for color in range(n))
        return res if res != float('Inf') else -1
            
            