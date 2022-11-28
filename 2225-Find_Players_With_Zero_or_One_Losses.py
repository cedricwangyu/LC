from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        teams = set()
        for w, l in matches:
            teams.add(w)
            teams.add(l)
            d[l] += 1
            
        answer = [[], []]
        for team in sorted(list(teams)):
            if d[team] == 0:
                answer[0].append(team)
            elif d[team] == 1:
                answer[1].append(team)
        return answer
            