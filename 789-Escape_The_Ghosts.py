class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return True if abs(target[0]) + abs(target[1]) < min(abs(i - target[0]) + abs(j - target[1]) for i, j in ghosts) else False
