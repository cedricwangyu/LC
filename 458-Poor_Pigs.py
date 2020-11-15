import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets) / math.log(int(minutesToTest / minutesToDie) + 1))