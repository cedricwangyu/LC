class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for p, s in zip(position, speed): time.append((p, (target-p)/s))
        time.sort(key=lambda x: x[0])
        curr_time, res = 0, 0
        for _, t in time[::-1]:
            if t > curr_time: curr_time, res = t, res+1
        return res
