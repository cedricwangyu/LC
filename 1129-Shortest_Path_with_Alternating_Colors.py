from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        p = [defaultdict(set), defaultdict(set)]
        for a, b in redEdges:
            p[0][a].add(b)
        for a, b in blueEdges:
            p[1][a].add(b)
        
        res, todo, seen = [0] + [-1] * (n-1), [(0, 0, 0), (0, 0, 1)], {(0, 0), (0, 1)}
        while todo:
            node, length, prev_color = todo.pop(0)
            if node in p[1-prev_color]: 
                for next_node in p[1-prev_color][node]:
                    if (next_node, 1-prev_color) not in seen:
                        seen.add((next_node, 1-prev_color))
                        res[next_node] = length+1 if res[next_node] < 0 else res[next_node]
                        todo.append((next_node, length+1, 1-prev_color))
        
        return res