import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        p = [[] for _ in range(len(searchWord))]
        for pr in products:
            i = 0
            while i < min(len(pr), len(searchWord)) and pr[i] == searchWord[i]: i += 1
            for j in range(i):
                bisect.insort_left(p[j], pr)
                if len(p[j]) > 3: p[j].pop()
        return p
