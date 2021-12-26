class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        curr = 0
        i = 0
        while i < n and fruits[i][0] < startPos - k:
            i += 1
        j = i
        res = 0
        while j < n and fruits[j][0] <= startPos + k:
            x, m = fruits[j]
            curr += m
            y = min(startPos - k + 2 * (x - startPos), startPos - (startPos + k - x) // 2)
            while fruits[i][0] < startPos and fruits[i][0] < y:
                curr -= fruits[i][1]
                i += 1
            res = max(res, curr)
            j+=1
        return res
