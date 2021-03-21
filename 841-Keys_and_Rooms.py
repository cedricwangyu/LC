class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        not_visit, visiting = {i for i in range(1, len(rooms))}, {0}
        while len(visiting) > 0:
            visiting = not_visit.intersection({j for i in visiting for j in rooms[i]})
            not_visit.difference_update(visiting)
        return False if len(not_visit) > 0 else True