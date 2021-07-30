class MapSum:
    def __init__(self):
        self.p = {}
        self.history = {}
    def insert(self, key: str, val: int) -> None:
        q = self.p
        for c in key:
            if c in q: q[c][0] = q[c][0] + val if key not in self.history else q[c][0] + val - self.history[key]
            else: q[c] = [val, {}]
            q = q[c][1]
        self.history[key] = val
    def sum(self, prefix: str) -> int:
        q, v = self.p, 0
        for c in prefix:
            if c in q: v, q = q[c][0], q[c][1]
            else: return 0
        return v
