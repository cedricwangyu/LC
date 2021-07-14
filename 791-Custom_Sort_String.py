class Solution:
    def customSortString(self, order: str, stri: str) -> str:
        p = {string.ascii_lowercase[i]: i + 26 for i in range(26)}
        for i in range(len(order)): p[order[i]] = i
        return "".join(sorted(list(stri), key=lambda x: p[x]))
