class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m, res = float('Inf'), []
        for i in range(len(arr)-1):
            curr = arr[i+1] - arr[i]
            if curr < m:
                m = curr
                res.clear()
                res.append([arr[i], arr[i+1]])
            elif curr == m:
                res.append([arr[i], arr[i+1]])
        return res
        
