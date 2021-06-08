class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        ## Keep track of min and fill the distance to start as 0.
        T = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
        T[start[0]][start[1]] = 0

        stack = [(0,start)]
        visited = {}

        while stack:
            # Extract the minimum distance value from the stack.
            _, node = heapq.heappop(stack)
            x,y = node
            
            # get the next edge from all 4 directions.
            d = [(1,0),(-1,0),(0,1),(0,-1)]
            for n in d:
                a,b = x,y
                dx,dy = n
                distance = 0

                while a+dx >= 0 and b+dy >= 0 and a+dx < len(maze) and b+dy < len(maze[0]) and maze[a+dx][b+dy] != 1:
                    distance += 1
                    a += dx
                    b += dy
                
                T[a][b] = min(T[a][b], T[x][y]+distance)

                if (a,b) != (x,y) and (a,b) not in visited:
                    visited[(a,b)] = True            
                    stack.append((T[a][b], (a,b)))

        ans = T[destination[0]][destination[1]]

        return  ans if ans != float('inf') else -1
