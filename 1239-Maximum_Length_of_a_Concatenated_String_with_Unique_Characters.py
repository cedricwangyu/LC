class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.curr = ""
        def dfs(i):
            if len(self.curr) > len(set(self.curr)): return 0
            if i >= len(arr): return len(self.curr)
            a1 = dfs(i+1)
            self.curr += arr[i]
            a2 = dfs(i+1)
            self.curr = self.curr[:-len(arr[i])]
            return max(a1, a2)
        return dfs(0)
