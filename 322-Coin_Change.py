# Brutal Force:
#
# def coinC(coins: List[int], c_pos: int, amount: int):
#     if c_pos >= len(coins):
#         return -1
#     if amount == 0:
#         return 0
    
#     maxi = int(amount / coins[c_pos])
#     mini = -1
#     for a in range(maxi, -1, -1):
#         res = amount - a * coins[c_pos]
#         if (res == 0):
#             #print("{} = {} - {} * {} ".format(res, amount, a, coins[c_pos]))
#             return a
#         else:
#             add = [coinC(coins, s, res) for s in range(c_pos + 1, len(coins), 1)]
#             if any([item >= 0 for item in add]):
#                 if mini == -1:
#                     mini = min([item + a for item in add if item >= 0])
#                 else:
#                     mini = min([min([item + a for item in add if item >= 0]), mini])
    
#     return mini

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1     
        