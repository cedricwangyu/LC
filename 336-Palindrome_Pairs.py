class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palin(w):
            return True if w == w[::-1] else False
        pre, aft, res = {}, {}, []
        for w in words:
            pre[w], aft[w] = {w[::-1]}, {w[::-1]}
            for i in range(len(w)):
                if is_palin(w[i::-1]): pre[w].add(w[:i:-1])
                if is_palin(w[i:]): 
                    if i > 0: aft[w].add(w[i-1::-1])
                    else: aft[w].add("")
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in pre[words[j]] or words[j] in aft[words[i]]: res.append([i, j])
                if words[i] in aft[words[j]] or words[j] in pre[words[i]]: res.append([j, i])
        return res
