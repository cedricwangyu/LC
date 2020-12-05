class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        vacant = 0
        res = 0
        free = 1
        for v in flowerbed:
            if v == 0: vacant += 1
            elif vacant > 0 and v == 1:
                res += (vacant + free - 1) // 2
                free = 0
                vacant = 0
                if res >= n: return True
            else: free = 0
        free += 1
        res += (vacant + free - 1) // 2
        if res >= n: return True
        else: return False
        