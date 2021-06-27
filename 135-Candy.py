class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]: candy.append(candy[-1] + 1)
            else: candy.append(1)
        prev, curr, res = 1, 0, candy[-1]
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]: curr, res, prev = prev + 1, res + max(candy[i], prev + 1), prev + 1
            else: curr, prev, res = 1, 1, res + candy[i]
        return res
