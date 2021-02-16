class Solution:
    def __init__(self):
        self.temp = ""
    def letterCasePermutation(self, S: str) -> List[str]:
        res, inds = [], [i for i in range(len(S)) if S[i].isalpha()]
        def helper(i):
            if i == 0: self.temp = S[:inds[0]]
            elif i >= len(inds): 
                res.append(self.temp + S[inds[-1] + 1:])
                self.temp = self.temp[:-1]
                return
            else: self.temp += S[inds[i - 1] + 1: inds[i]]
            self.temp += S[inds[i]].lower()
            helper(i + 1)
            self.temp += S[inds[i]].upper()
            helper(i + 1)
            if i > 0: self.temp = self.temp[:inds[i-1]]
        if len(inds) > 0: 
            helper(0)
            return res
        else: return [S]
        