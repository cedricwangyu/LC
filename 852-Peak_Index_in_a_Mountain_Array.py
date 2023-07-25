class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while r > l+2:
            m = (l + r) // 2
            if arr[m] < arr[m+1]:
                l = m
            elif arr[m] < arr[m-1]:
                r = m
            else:
                return m
        return (l + r) // 2

