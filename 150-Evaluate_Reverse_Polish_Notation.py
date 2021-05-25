class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t[-1].isdigit(): s.append(int(t))
            else:
                if t is '+': s[-2] += s[-1]
                elif t is '-': s[-2] -= s[-1]
                elif t is '*': s[-2] *= s[-1]
                else: s[-2] = int(s[-2] / s[-1])   
                s.pop()
        return s[0]
