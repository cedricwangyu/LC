class Solution:
    def countElements(self, arr: List[int]) -> int:
        p = collections.Counter(arr)
        return sum(p[n] if n+1 in p else 0 for n in p)
