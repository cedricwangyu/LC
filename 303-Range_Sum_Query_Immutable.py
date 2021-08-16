class NumArray:

    def __init__(self, nums: List[int]):
        self.p = list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        sec = 0 if left == 0 else self.p[left - 1]
        return self.p[right] - sec

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
