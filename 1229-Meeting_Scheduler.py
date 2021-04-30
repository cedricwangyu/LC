class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x)
        slots2.sort(key=lambda x: x)
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] <= slots2[j][0]: i += 1
            elif slots1[i][0] >= slots2[j][1]: j += 1
            else:
                start, end = max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])
                if end - start >= duration: return [start, start + duration]
                if slots1[i][1] > slots2[j][1]: j += 1
                elif slots1[i][1] < slots2[j][1]: i += 1
                else: i, j = i+1, j+1
        return []