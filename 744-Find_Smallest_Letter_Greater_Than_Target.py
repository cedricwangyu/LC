from bisect import bisect_right
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect_right(letters, target)
        return letters[i] if i < len(letters) else letters[0]