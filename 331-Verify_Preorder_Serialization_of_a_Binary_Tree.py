class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        self.p = preorder.split(',')
        if len(self.p) % 2 < 1: return False
        def helper():
            if len(self.p) <= 0: return False
            else:
                c = self.p.pop(0)
                if c == '#': return True
                return helper() and helper()
        return True if helper() and len(self.p) == 0 else False       
