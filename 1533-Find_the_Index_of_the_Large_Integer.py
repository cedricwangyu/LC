# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        L, R = 0, reader.length()-1
        while R - L > 0:
            M = (R + L) // 2
            if M - L + 1 > R - M:
                res = reader.compareSub(L, M-1, M+1, R)
                if res > 0:
                    R = M-1
                elif res < 0:
                    L = M+1
                else:
                    return M
            else:
                res = reader.compareSub(L, M, M+1, R)
                if res > 0:
                    R = M
                else:
                    L = M+1
        return L
