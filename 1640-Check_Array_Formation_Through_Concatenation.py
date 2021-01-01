class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if any([item[0] not in set(arr) for item in pieces]): return False
        pieces.sort(key = lambda x: arr.index(x[0]))
        arr2 = [item for x in pieces for item in x]
        if len(arr) == len(arr2): return all([arr[i] == arr2[i] for i in range(len(arr))])
        else: return False