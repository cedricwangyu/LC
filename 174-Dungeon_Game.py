class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [0] * len(dungeon[-1])
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dp)-1, -1, -1):
                if i == len(dungeon)-1 and j == len(dp)-1: dp[j] = 1 - dungeon[i][j]
                elif i == len(dungeon)-1: dp[j] = dp[j+1] - dungeon[i][j]
                elif j == len(dp)-1: dp[j] -= dungeon[i][j]
                else: dp[j] = min(dp[j], dp[j+1]) - dungeon[i][j]
                if dp[j] < 1: dp[j] = 1
        return dp[0]
