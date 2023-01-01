class Solution:
    def confusingNumber(self, n: int) -> bool:
        p = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        res = ""
        for num in str(n):
            if num not in p:
                return False
            else:
                res = p[num] + res
        return int(res) != n