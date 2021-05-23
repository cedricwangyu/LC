class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        self.over = [[0] * len(words) for _ in range(len(words))]
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j: continue
                k = 1
                while k <= len(words[i]) and k <= len(words[j]):
                    if words[i][-k:] == words[j][:k]: self.over[i][j] = k
                    k += 1
        p, q = {('0' * i + '1' + '0' * (len(words) - i - 1), i): (0, (i,)) for i in range(len(words))}, {}
        for _ in range(len(words) - 1):
            for key in p:
                for i, c in enumerate(key[0]):
                    if c == '0':
                        new_key = (key[0][:i] + '1' + key[0][i+1:], i)
                        if new_key not in q: q[new_key] = (self.over[key[1]][i] + p[key][0], p[key][1] + (i,))
                        elif q[new_key][0] < self.over[key[1]][i] + p[key][0]: q[new_key] = (self.over[key[1]][i] + p[key][0], p[key][1] + (i,))
                        del new_key
            p, q = q, p
            q.clear()
        M, Mrec = 0, tuple(i for i in range(len(words)))
        for key in p:
            if p[key][0] > M: M, Mrec = p[key]
        res = ""
        for i, idx in enumerate(Mrec):
            if i == 0: res += words[idx]
            else: res += words[idx][self.over[Mrec[i-1]][idx]:]
        return res    