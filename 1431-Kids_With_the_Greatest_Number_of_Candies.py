class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        required = max(candies) - extraCandies
        return [c >= required for c in candies]