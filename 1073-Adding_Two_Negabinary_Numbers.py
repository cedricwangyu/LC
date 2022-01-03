class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) < len(arr2): arr1, arr2 = arr2, arr1
        for i in range(-1, -len(arr2)-1, -1): arr1[i] += arr2[i]
        for i in range(len(arr1)-1, 0, -1):
            if arr1[i] >= 2: arr1[i], arr1[i-1] = arr1[i]-2, arr1[i-1]-1
            elif arr1[i] == -1: arr1[i], arr1[i-1] = 1, arr1[i-1]+1 
        if arr1[0] >= 2: 
            arr1[0] -= 2
            arr1 = [1, 1] + arr1
        elif arr1[0] == -1:
            arr1[0] = 1
            arr1 = [1] + arr1
        else:
            while len(arr1) > 0 and arr1[0] == 0: arr1.pop(0)
            if len(arr1) == 0: arr1.append(0)
        return arr1
