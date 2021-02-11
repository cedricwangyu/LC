from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counters = Counter(s)
        countert = Counter(t)
        for key in counters.keys():
            if key in countert and countert[key] == counters[key]: del countert[key]
            else: return False
        
        if len(countert.keys()) <= 0: return True
        else: return False