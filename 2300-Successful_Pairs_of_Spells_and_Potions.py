from bisect import bisect_right
import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        for i in range(m):
            potions[i] = math.ceil(success / potions[i])
        potions.sort()
        return [bisect_right(potions, s) for s in spells]