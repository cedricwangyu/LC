class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while len(pushed) > 0 or len(popped) > 0:
            if len(stack) <= 0: stack.append(pushed.pop(0))
            else:
                if len(popped) > 0 and popped[0] == stack[-1]:
                    stack.pop()
                    popped.pop(0)
                elif len(pushed) > 0: stack.append(pushed.pop(0))
                else: return False
        return True