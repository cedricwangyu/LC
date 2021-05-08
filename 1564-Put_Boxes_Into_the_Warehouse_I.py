import bisect
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        M = warehouse[0]
        for i in range(len(warehouse)):
            M = min(M, warehouse[i])
            warehouse[i] = M
        boxes.sort()
        res = 0
        for i in range(len(warehouse)-1, -1, -1):
            j = bisect.bisect_right(boxes, warehouse[i])
            if j > 0: 
                res += 1
                boxes.pop(j-1)
        return res