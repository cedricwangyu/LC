class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: 
            return "1"
        curr_char, curr_count, res = "", 0, ""
        for c in self.countAndSay(n-1):
            if c == curr_char:
                curr_count += 1
            else:
                if curr_count > 0:
                    res += str(curr_count) + curr_char
                curr_char, curr_count = c, 1
        return res + str(curr_count) + curr_char