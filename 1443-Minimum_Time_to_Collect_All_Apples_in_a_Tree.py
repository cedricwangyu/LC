from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.p = defaultdict(list)
        for a, b in edges:
            self.p[a].append(b)
            self.p[b].append(a)
        
        self.curr = {0,}
        def dfs(idx):
            res, res_has_apple = 0, hasApple[idx]
            for new_idx in self.p[idx]:
                if new_idx not in self.curr:
                    self.curr.add(new_idx)
                    length, has_apple = dfs(new_idx)
                    res_has_apple = has_apple or res_has_apple
                    if has_apple:
                        res += 2 + length
                    self.curr.remove(new_idx)
            return res, res_has_apple 
        
        res, _ = dfs(0)
        return res