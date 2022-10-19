import collections
import bisect
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        res = []
        for word in counter:
            count = counter[word]
            if len(res) < k:
                bisect.insort_left(res, (-count, word))
            elif (-count, word) < res[0]:
                res.insert(0, (-count, word))
            elif (-count, word) > res[-1]:
                pass
            else:
                bisect.insort_left(res, (-count, word))
            if len(res) > k:
                res.pop()
        return [word for _, word in res]
        
        