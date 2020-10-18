class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        i = 1
        while i < len(prices):
            if prices[i] == prices[i - 1]:
                prices.pop(i)
            else:
                i += 1
        trend = []
        start = prices[0]
        for i, p in enumerate(prices):
            if i == 0:
                continue
            elif i == len(prices) -1:
                trend.append(p - start)
            else:
                if (prices[i+1] <= p and prices[i-1] <= p) or (prices[i+1] >= p and prices[i-1] >= p):
                    trend.append(p - start)
                    start = p
        if trend == []:
            return 0
        elif len(trend) == 1:
            if trend[0] >= 0 and k >= 1:
                return trend[0]
            else:
                return 0
            
        if trend[0] <= 0:
            trend.pop(0)
        if trend[-1] <= 0:
            trend.pop(-1)
        
        print(trend)
        if k == 0 :
            return 0
        while(k < int(len(trend)/2) + 1):
            temp = [abs(item) for item in trend]
            ind = temp.index(min(temp))
            if ind == 0:
                del trend[:2]
            elif ind == len(trend) - 1:
                del trend[-2:]
            else:
                m = sum(trend[ind - 1: ind + 2])
                del trend[ind - 1: ind + 2]
                trend.insert(ind - 1, m)
        
        res = sum(trend[::2])
        return res
                             
            