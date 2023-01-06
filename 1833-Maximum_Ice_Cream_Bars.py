from collections import Counter
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = Counter(costs)
        costs = sorted([(price, costs[price]) for price in costs])
        res = 0
        for price, amount in costs:
            max_num = coins // price
            remain = coins 
            if max_num > amount:
                res += amount
                coins -= amount * price
            else:
                return res + max_num

        return res
            
                



