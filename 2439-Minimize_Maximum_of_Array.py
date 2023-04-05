from math import ceil
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr, room = 0, 0
        for i, n in enumerate(nums):
            if n > curr:
                room -= n - curr
                if room < 0:
                    addition = ceil((- room) / (i + 1))
                    room += addition * (i + 1)
                    curr += addition
            else:
                room += curr - n
        return curr