class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0: return []
        res, aa, bb = [], -2, -1
        if firstList[0][0] < secondList[0][0]: A, B = firstList, secondList
        else: B, A = firstList, secondList
        while len(A) > 0:
            a, b = A.pop(0)
            if b < aa: pass
            elif a > bb: aa, bb, A, B = a, b, B, A
            else:
                res.append([max(a, aa), min(b, bb)])
                if b > bb: aa, bb, A, B = a, b, B, A
        return res
