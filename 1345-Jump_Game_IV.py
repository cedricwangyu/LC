class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        p = {}
        for i, n in enumerate(arr):
            if n in p: p[n].append(i)
            else: p[n] = [i]

        state = [0] * len(arr)
        state[0], state[-1] = 1, -1
        front1, front2 = [0], [len(arr) - 1]
        for i in range(1, len(arr)):
            if i % 2 == 0: front, new, mark = front1, [], 1
            else: front, new, mark = front2, [], -1
            for f in front: 
                for ff in p[arr[f]] + [min(f + 1, len(arr) - 1), max(f - 1, 0)]:
                    if state[ff] == -mark: return i
                    elif state[ff] == 0:
                        new.append(ff)
                        state[ff] = mark
            front.clear()
            front.extend(new)
            
        