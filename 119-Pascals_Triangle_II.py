class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        old, new = [1], [1, 1]
        if rowIndex == 0: 
            return old
        elif rowIndex == 1:
            return new
        for _ in range(2, rowIndex+1):
            old, new = new, old
            new.clear()
            new.append(1)
            for i in range(1, len(old)):
                new.append(old[i] + old[i-1])
            new.append(1)
        return new

