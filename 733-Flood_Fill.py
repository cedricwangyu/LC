class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color, todo = image[sr][sc], [(sr, sc)]
        if color == newColor: return image
        while len(todo) > 0:
            r, c = todo.pop(0)
            image[r][c] = newColor
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == color: todo.append((nr, nc))
        return image
