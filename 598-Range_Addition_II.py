class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min(item[0] for item in ops) * min(item[1] for item in ops) if len(ops) > 0 else m*n
