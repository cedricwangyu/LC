class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num): return "0"
        remain = k
        i = 0
        while i < len(num)-remain:
            min_idx, curr = i, 10
            for j in range(i, min(i+remain+1, len(num))):
                if int(num[j]) < curr: min_idx, curr = j, int(num[j])
                if curr == 0: break
            num, remain, i = num[:i] + num[min_idx:], remain - min_idx + i, i+1
            if remain <= 0: break
        return str(int(num[:len(num)-remain]))
            