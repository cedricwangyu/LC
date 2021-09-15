class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        s, res = 0, 1
        for i in range(1, len(arr)):
            if i == 1: res = 1 if arr[0] == arr[1] else 2
            elif (arr[i-1] > arr[i-2] and arr[i] < arr[i-1]) or (arr[i-1] < arr[i-2] and arr[i] > arr[i-1]): res = max(res, i - s + 1)
            else: s = i - 1
        return res