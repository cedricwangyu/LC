class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        todo, seen, dirs = [tuple(start)], {tuple(start)}, ((1, 0), (-1, 0), (0, 1), (0, -1))
        while todo:
            i, j = todo.pop()
            for di, dj in dirs:
                ci, cj = i, j
                while 0 <= ci+di < len(maze) and 0 <= cj+dj < len(maze[0]) and maze[ci+di][cj+dj] != 1:
                    ci, cj = ci+di, cj+dj
                
                if (ci, cj) == tuple(destination):
                    return True
                if (ci, cj) not in seen:
                    todo.append((ci, cj))
                    seen.add((ci, cj))

        return False    

