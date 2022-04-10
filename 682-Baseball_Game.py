class Solution(object):
    def calPoints(self, ops):
        stack = []
        res = 0
        for op in ops:
            if op == '+':
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                res -= stack.pop()
            elif op == 'D':
                res += 2 * stack[-1]
                stack.append(2 * stack[-1])
            else:
                res += int(op)
                stack.append(int(op))
        return res