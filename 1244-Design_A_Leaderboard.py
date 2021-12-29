class Leaderboard:

    def __init__(self):
        self.player_score = collections.defaultdict(int)
        self.score_player = collections.defaultdict(set)
        self.score = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.player_score:
            self.player_score[playerId] = score
            self.score_player[score].add(playerId)
            bisect.insort(self.score, score)
        else:
            self.score_player[self.player_score[playerId]].remove(playerId)
            self.score.pop(bisect.bisect_left(self.score, self.player_score[playerId]))
            self.player_score[playerId] += score
            self.score_player[self.player_score[playerId]].add(playerId)
            bisect.insort(self.score, self.player_score[playerId])
            
            

    def top(self, K: int) -> int:
        return sum(self.score[-K:])

    def reset(self, playerId: int) -> None:
        self.score_player[self.player_score[playerId]].remove(playerId)
        self.score.pop(bisect.bisect_left(self.score, self.player_score[playerId]))
        self.player_score[playerId] = 0
        self.score_player[self.player_score[playerId]].add(playerId)
        bisect.insort(self.score, self.player_score[playerId])


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
