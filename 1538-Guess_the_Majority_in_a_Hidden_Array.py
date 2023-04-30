# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        a, b, c, d = reader.query(0,1,2,3), reader.query(1,2,3,4), reader.query(0,1,2,4), reader.query(0,1,3,4)
        if a == b:
            if a == 0:
                if c == 0:
                    curr, idx = [0, 1, 1, 0, 0], 1
                elif d == 0:
                    curr, idx = [0, 1, 0, 1, 0], 1
                else:
                    curr, idx = [0, 0, 1, 1, 0], 2
            elif a == 2:
                if c == 0:
                    curr, idx = [0, 1, 1, 1, 0], 1
                elif c == 2:
                    curr, idx = ([0, 0, 1, 0, 0], 2) if d == 4 else ([0, 1, 0, 0, 0], 1)
                else:
                    curr, idx = [0, 0, 0, 1, 0], 3
            else:
                curr, idx = [0, 0, 0, 0, 0], None
        else:
            idx = 4
            if (a, b) == (0, 2):
                if c == 0:
                    curr = [0, 0, 1, 1, 1] if d == 0 else [0, 1, 0, 1, 1]
                else:
                    curr = [0, 1, 1, 0, 1]
            elif (a, b) == (2, 0):
                if c == 0:
                    curr = [0, 1, 0, 0, 1] if d == 0 else [0, 0, 1, 0, 1]
                else:
                    curr = [0, 0, 0, 1, 1]
            elif (a, b) == (2, 4):
                curr = [0, 1, 1, 1, 1]
            else:
                curr = [0, 0, 0, 0, 1]
        curr_res, count = b, sum(curr)
        count = [5 - count, count]
        curr.pop(0)
        for i in range(5, reader.length()):
            new_res = reader.query(i-3, i-2, i-1, i)
            if new_res == curr_res:
                curr.append(curr.pop(0))
            else:
                curr.append(1 - curr.pop(0))
            count[curr[-1]] += 1
            curr_res = new_res
            if curr[-1] == 1 and idx is None:
                idx = i
        
        if count[0] > count[1]:
            return 0
        elif count[0] < count[1]:
            return idx
        else:
            return -1
            









