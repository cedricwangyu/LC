class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx = set()
        self.vec = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.idx.add(i)
                self.vec[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for idx in self.idx.intersection(vec.idx):
            res += self.vec[idx] * vec.vec[idx]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
