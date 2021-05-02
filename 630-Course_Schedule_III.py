import bisect
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        q, time = [], 0
        for c in courses:
            if (time + c[0] <= c[1]):
                bisect.insort_left(q, c[0])
                time += c[0]
            elif (len(q) > 0 and q[-1] > c[0]):
                time += c[0] - q.pop()
                bisect.insort_left(q, c[0])
        return len(q)