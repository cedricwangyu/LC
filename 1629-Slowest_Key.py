class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes.insert(0, 0)
        return max((releaseTimes[i+1] - releaseTimes[i], keysPressed[i]) for i in range(len(keysPressed)))[1]
