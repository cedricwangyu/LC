class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.p = []
        for item in vec:
            self.p += item
        print(self.p)
        self.i = -1

    def next(self) -> int:
        self.i += 1
        return self.p[self.i]

    def hasNext(self) -> bool:
        return True if self.i < len(self.p)-1 else False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()