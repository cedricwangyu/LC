class Solution:
    def average(self, salary: List[int]) -> float:
        Sum, Min, Max = 0, min(salary[0:2]), max(salary[0:2])
        for s in salary[2:]:
            if s < Min:
                Sum, Min = Sum + Min, s
            elif s > Max:
                Sum, Max = Sum + Max, s
            else:
                Sum += s
        
        return Sum / (len(salary)-2)

            