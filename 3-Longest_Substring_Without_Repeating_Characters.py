class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, state, res = 0, 0, set(), 0
        while right < len(s):
            state.add(s[right])
            if right - left + 1 > len(state):
                while s[left] != s[right]:
                    state.remove(s[left])
                    left += 1
                left += 1
            res = max(res, len(state))
            right += 1
        return res
        
        