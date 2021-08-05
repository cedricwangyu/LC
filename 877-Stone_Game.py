class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.lru_cache(maxsize=125250)
        def dp(i, j):
            if i > j: return (0, 0)
            idx = int((i + j) % 2 == 0)
            p1, p2, res = dp(i+1, j), dp(i, j-1), [0, 0]
            if p1[idx] + piles[i] > p2[idx] + piles[j]: res[idx], res[1-idx] = p1[idx] + piles[i], p1[1-idx]
            else: res[idx], res[1-idx] = p2[idx] + piles[j], p2[1-idx]
            return tuple(res)
        return dp(0, len(piles) -1)