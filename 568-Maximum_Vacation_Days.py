class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        p, q = [d[-1] for d in days], [0] * len(flights)
        for i in range(len(flights)): flights[i][i] = 1
        for j in range(len(days[0])-2, -1, -1):
            p, q = q, p
            for i in range(len(days)):
                curr = 0
                for jj in range(len(flights[0])):
                    if flights[i][jj]: curr = max(curr, q[jj])
                p[i] = curr + days[i][j]
        return max(p[i] for i in range(len(p)) if flights[0][i])
