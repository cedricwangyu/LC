class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        d_len = 0
        for s in S:
            if s.isdigit():
                d_len *= int(s)
                new_K = K % (d_len // int(s))
                new_K = new_K if new_K is not 0 else (d_len // int(s))
                if d_len >= K: return self.decodeAtIndex(S, new_K)
            else:
                d_len += 1
                if d_len >= K: return s