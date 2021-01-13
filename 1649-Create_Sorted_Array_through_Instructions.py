from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sorted_list, cost = SortedList(), 0
        for i in range(len(instructions)):
            left_cost = sorted_list.bisect_left(instructions[i])
            right_cost = i - sorted_list.bisect_right(instructions[i])
            cost += min(left_cost, right_cost)
            sorted_list.add(instructions[i])
        return cost % (10**9 + 7)