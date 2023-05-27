class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[0, 0]]
        for i in range(n-1, -1, -1):
            curr0, max0, max1 = 0, -float('Inf'), 0
            for j, (a, b) in enumerate(dp):
                curr0 += stoneValue[i+j]
                if curr0 + b - a > max0 - max1:
                    max0, max1 = curr0 + b, a
            dp.insert(0, [max0, max1])
            if len(dp) > 3:
                dp.pop()

        if dp[0][0] > dp[0][1]: return 'Alice'
        elif dp[0][0] < dp[0][1]: return 'Bob'
        else: return 'Tie'
