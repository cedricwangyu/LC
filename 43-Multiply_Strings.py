class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0': return '0'
        m, n, p, res = len(num1), len(num2), defaultdict(int), ""
        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                c = m+n-i-j-2
                p[c] += int(d1)*int(d2)
                while p[c] >= 10: p[c], p[c+1], c = p[c] % 10, p[c+1]+p[c] // 10, c+1
        for i in range(500):
            if i in p: res = str(p[i]) + res
        return res
