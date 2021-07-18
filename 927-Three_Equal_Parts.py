class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        try: i, j = next(_ for _ in range(len(arr)) if arr[_] > 0), len(arr) - 1
        except: return [0, len(arr)-1]
        l, r = str(arr[i]), str(arr[j])
        while i + 1 < j:
            if l == r: 
                try: ii = next(_ for _ in range(i+1, j) if arr[_] > 0)
                except: return [i, j] if int(l) == 0 else [-1, -1]
                if j - ii >= len(arr) - j and l == "".join(str(s) for s in arr[ii: ii + len(arr) - j]) and all(i == 0 for i in arr[ii+len(arr)-j: j]): return [i, ii+len(arr)-j]
            i, j, l, r = i + 1, j - 1, l + str(arr[i+1]), str(arr[j-1]) + r
        return [-1, -1]
