class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        res = 0
        while len(boxTypes) > 0 and truckSize >= boxTypes[0][0]:
            res, truckSize = res + boxTypes[0][0] * boxTypes[0][1], truckSize - boxTypes[0][0]
            boxTypes.pop(0)
        return res + truckSize * boxTypes[0][1] if len(boxTypes) > 0 else res
