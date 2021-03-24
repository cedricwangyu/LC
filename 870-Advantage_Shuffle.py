class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort(reverse=True)
        br, res, i = sorted(enumerate(B), key=lambda x: x[1], reverse=True), [0] * len(A), 0
        while len(A) > 0:
            info = br.pop(0)
            if A[0] > info[1]: res[info[0]] = A.pop(0)
            else: res[info[0]] = A.pop(-1)
        return res