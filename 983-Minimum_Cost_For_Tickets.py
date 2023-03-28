class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp, pass_expire_id = [0] * n, [n-1, n-1]
        for i in range(n-1, -1, -1):
            curr_day = days[i]
            while days[pass_expire_id[0]] - curr_day > 6:
                pass_expire_id[0] -= 1
            while days[pass_expire_id[1]] - curr_day > 29:
                pass_expire_id[1] -= 1
            
            buy_one = costs[0] if i == n-1 else costs[0] + dp[i+1]
            buy_seven = costs[1] if pass_expire_id[0] == n-1 else costs[1] + dp[pass_expire_id[0]+1]
            buy_thirty = costs[2] if pass_expire_id[1] == n-1 else costs[2] + dp[pass_expire_id[1]+1]
            dp[i] = min(buy_one, buy_seven, buy_thirty)
        
        return dp[0]

