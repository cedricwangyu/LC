class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2 or arr[1] < arr[0]: return False
        inc = True
        for i in range(1, len(arr)):
            if inc and arr[i] > arr[i - 1]: pass
            elif inc and arr[i] < arr[i - 1]: inc = False
            elif not inc and arr[i] > arr[i - 1]: return False
            elif not inc and arr[i] < arr[i - 1]: pass
            else: return False
        
        if not inc: return True
        else: return False
        