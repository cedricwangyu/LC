class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        curr_color = colors[0]
        curr_sum = neededTime[0]
        curr_max = neededTime[0]
        res = 0
        for color, time in zip(colors[1:], neededTime[1:]):
            if color == curr_color:
                curr_sum += time
                if time > curr_max:
                    curr_max = time
            else:
                curr_color = color
                res += curr_sum - curr_max
                curr_sum = time
                curr_max = time
        res += curr_sum - curr_max
        return res