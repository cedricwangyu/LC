class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = []
        for n in nums:
            bisect.insort(self.q, n)
            if len(self.q) > k: self.q.pop(0)
        

    def add(self, val: int) -> int:
        if len(self.q) < self.k: heapq.heappush(self.q, val)
        else: heapq.heappushpop(self.q, val)
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)