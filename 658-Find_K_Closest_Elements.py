class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect.bisect_left(arr, x)
        l = max(ind - k, 0)
        while l + k < len(arr) and abs(arr[l + k] - x) < abs(arr[l] - x): l += 1
        return arr[l:l+k]
