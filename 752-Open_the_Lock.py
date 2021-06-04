class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        todo, visited, deadends = [('0000', 0)], {'0000'}, set(deadends)
        while len(todo) > 0:
            curr, curr_step = todo.pop(0)
            if curr == target: return curr_step
            elif curr in deadends: continue
            for c in [curr[:i] + str((int(curr[i]) + 1) % 10) + curr[i+1:] for i in range(4)] + [curr[:i] + str((int(curr[i]) - 1) % 10) + curr[i+1:] for i in range(4)]:
                if c not in visited: 
                    todo.append((c, curr_step + 1))
                    visited.add(c)
        return -1
