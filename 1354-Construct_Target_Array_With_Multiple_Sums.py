import bisect
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        target.sort()
        S = sum(target)
        while target[-1] > 1:
            n = target.pop()
            S -= n
            if n <= S or len(target) == 0: return False
            if S > 1: n %= S
            else: return True
            if n == 0: return False
            bisect.insort_left(target, n)
            S += n
        return True