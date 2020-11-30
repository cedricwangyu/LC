class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        value = [True if item == 0 else False for item in arr]
        if any(value) is False: return False
        n, change = len(arr), True
        while change:
            change = False
            for i in range(n):
                if value[i]: continue
                elif i + arr[i] < n and value[i + arr[i]]:
                    value[i] = True
                    change = True
                elif i - arr[i] >= 0 and value[i - arr[i]]:
                    value[i] = True
                    change = True
        return value[start]
        
        