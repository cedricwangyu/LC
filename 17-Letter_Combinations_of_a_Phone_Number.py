class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        def helper(i, curr):
            if i >= len(digits):
                self.res.append(curr)
                return
            n = int(digits[i])
            start = (n - 2) * 3 if n <= 7 else  (n - 2) * 3 + 1
            end = start + 3 if n not in (7, 9) else start + 4
            for c in string.ascii_lowercase[start: end]: helper(i+1, curr + c)
        helper(0, "")
        return self.res if len(self.res) > 1 else []