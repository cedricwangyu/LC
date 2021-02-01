class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        res, diff = 0, - float("Inf")
        for nut in nuts: 
            d = abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])
            res += 2 * d
            diff = max(diff, d - abs(nut[0] - squirrel[0]) - abs(nut[1] - squirrel[1]))
        return res - diff
        