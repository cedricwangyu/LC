class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        dic, res = {}, []
        for word in words:
            if len(word) <= 3: continue
            curr = dic
            for i, c in enumerate(word[:-2]):
                if i == 0: key = (c+word[-1], len(word)-i-2)
                else: key = (c, len(word)-i-2)
                if key not in curr: curr[key] = [{}, 0]
                curr[key][1] += 1
                curr = curr[key][0]
        print(dic)
        for word in words:
            if len(word) <= 3: 
                res.append(word)
                continue
            curr = dic
            for i, c in enumerate(word[:-2]):
                if i == 0: key = (c+word[-1], len(word)-i-2)
                else: key = (c, len(word)-i-2)
                if curr[key][1] <= 1 or key[1] == 1:
                    if key[1] == 1: res.append(word)
                    else: res.append(word[:i+1] + str(key[1]) + word[-1])
                    break
                else: curr = curr[key][0]
        return res