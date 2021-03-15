class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        p = [1] * len(arr)
        for i in range(1, len(p)):
            q = {}
            for j in range(i):
                if arr[j] in q: p[i] += 2 * p[j] * p[q[arr[j]]]
                else:
                    if arr[j] ** 2 == arr[i]: p[i] += p[j] ** 2
                    elif arr[i] % arr[j] == 0:
                        q[arr[i] // arr[j]] = j
        return sum(p) % (10 ** 9 + 7)