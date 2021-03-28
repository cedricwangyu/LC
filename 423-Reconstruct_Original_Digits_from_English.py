class Solution:
    def __init__(self):
        self.p = [('x', 'six', 6), ('w', 'two', 2), ('z', 'zero', 0), ('u', 'four', 4), ('s', 'seven', 7), ('v', 'five', 5), ('o', 'one', 1), ('r', 'three', 3), ('g', 'eight', 8), ('n', 'nine', 9)]
    def originalDigits(self, s: str) -> str:
        c, res = collections.Counter(s), {i: 0 for i in range(10)}
        for item in self.p:
            while item[0] in c:
                res[item[2]] += 1
                for char in item[1]:
                    c[char] -= 1
                    if c[char] == 0: del c[char]
        return "".join(str(i) * res[i] for i in range(10))