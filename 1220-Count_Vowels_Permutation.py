class Solution:    
    def countVowelPermutation(self, n: int) -> int:
        p, curr_c, prev_c = ((1,2,4), (0,2), (1,3), tuple([2]), (2,3)), [0] * 5, [1] * 5
        for _ in range(n-1):
            for i in range(5):
                for idx in p[i]: curr_c[i] += prev_c[idx]
            prev_c = [0] * 5
            prev_c, curr_c = curr_c, prev_c
        return sum(prev_c) % (10 ** 9 + 7)
