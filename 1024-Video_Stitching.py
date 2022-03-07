class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        max_reach = [-1] * 101
        for start, end in clips:
            max_reach[start] = max(max_reach[start], end)
        prev_max, curr_max, count = float('-Inf'), 0, 0
        for i, max_r in enumerate(max_reach):
            curr_max = max(curr_max, max_r)
            if curr_max >= time: return count + 1
            if i >= prev_max:
                if curr_max <= i: return -1
                count += 1
                prev_max = curr_max
        return -1
                