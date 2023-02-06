from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        p = defaultdict(set)
        for w1, w2 in similarPairs:
            p[w1].add(w2)
            p[w2].add(w1)
        
        for w1, w2 in zip(sentence1, sentence2):
            if (w1 not in p or w2 not in p[w1]) and w1 != w2:
                return False
        return True
        
Console
