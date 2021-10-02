class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        total_array_sum = sum(arr)
        if total_array_sum % k != 0: return False
        target_sum = total_array_sum // k
        arr.sort(reverse=True)
        taken = [False] * n
        def backtrack(index, count, curr_sum):
            if count == k - 1: return True
            if curr_sum > target_sum: return False
            if curr_sum == target_sum: return backtrack(0, count + 1, 0)
            for j in range(index, n):
                if not taken[j]:
                    taken[j] = True
                    if backtrack(j + 1, count, curr_sum + arr[j]):  return True
                    taken[j] = False
            return False
        return backtrack(0, 0, 0)