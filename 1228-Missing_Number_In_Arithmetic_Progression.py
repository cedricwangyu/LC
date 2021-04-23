class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[-1] > arr[0]: step = min(arr[1] - arr[0], arr[-1] - arr[-2])
        elif arr[-1] < arr[0]: step = max(arr[1] - arr[0], arr[-1] - arr[-2])
        else: return arr[0]
        for i in range(1, len(arr)):
            if arr[i] - step != arr[i-1]: return arr[i] - step