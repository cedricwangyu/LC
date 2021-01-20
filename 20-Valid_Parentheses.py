class Solution:
    def isValid(self, s: str) -> bool:
        stack, link = [], {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in ['(', '{', '[']: stack.append(c)
            else:
                if len(stack) <= 0: return False
                if stack[-1] == link[c]: stack.pop()
                else: return False
        if len(stack) > 0: return False
        return True
                