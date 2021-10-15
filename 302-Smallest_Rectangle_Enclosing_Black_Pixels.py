class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        seen, todo, dirs, m, n, l, r, u, d = {(x, y)}, [(x, y)], ((0, 1), (0, -1), (-1, 0), (1, 0)), len(image), len(image[0]), y, y, x, x
        while todo:
            x, y = todo.pop(0)
            l, r, u, d = min(l, y), max(r, y), min(u, x), max(d, x)
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if (nx, ny) not in seen and 0 <= nx < m and 0 <= ny < n and image[nx][ny] == "1": 
                    todo.append((nx, ny))
                    seen.add((nx, ny))
        return (r-l+1)*(d-u+1)