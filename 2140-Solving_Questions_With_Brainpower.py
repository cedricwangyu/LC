class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        for i in range(len(questions)-2, -1, -1):
            dp[i] = questions[i][0]
            dp[i] = dp[i] if i + questions[i][1] + 1 >= n else dp[i] + dp[i + questions[i][1] + 1]
            dp[i] = max(dp[i], dp[i+1])
        return dp[0]