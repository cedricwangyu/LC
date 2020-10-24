# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        start = 0
        end = target - reader.get(start)
        if reader.get(start) == target:
            return 0
        elif reader.get(end) == target:
            return end
        elif reader.get(start) > target or reader.get(end) < target:
            return -1
        
        while end - start > 1:
            mid = int((end + start) / 2)
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                end = mid
            else:
                start = mid
                
        return -1
        
        