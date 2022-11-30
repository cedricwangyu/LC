from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        counter_counter = [counter[val] for val in counter]
        return len(set(counter_counter)) == len(counter_counter)