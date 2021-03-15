class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        p = [0] * (amount + 1)
        p[0] = 1
        for c in coins:
            for i in range(c, len(p)):
                p[i] += p[i - c]
        return p[-1]