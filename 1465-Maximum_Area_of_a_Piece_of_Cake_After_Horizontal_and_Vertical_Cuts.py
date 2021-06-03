class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        horizontalCuts.insert(0, 0)
        verticalCuts.append(w)
        verticalCuts.insert(0, 0)
        mh, mv = 0, 0
        for i in range(1, len(horizontalCuts)): mh = max(mh, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)): mv = max(mv, verticalCuts[i] - verticalCuts[i-1])
        return mh * mv % (10 ** 9 + 7)