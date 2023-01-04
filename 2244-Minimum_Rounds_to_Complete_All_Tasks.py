from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        p, res = Counter(tasks), 0
        for num in p:
            count = p[num]
            if count < 2:
                return -1
            else:
                res += count // 3
            if count % 3 > 0:
                res += 1
        return res