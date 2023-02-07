class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right, counter, res = 0, 0, {fruits[0]: 1}, 1
        while True:
            if len(counter) <= 2:
                res = max(res, right - left + 1)
                if right == len(fruits) - 1:
                    break
                right += 1
                if fruits[right] in counter:
                    counter[fruits[right]] += 1
                else:
                    counter[fruits[right]] = 1      
            else:
                if counter[fruits[left]] == 1:
                    del counter[fruits[left]]
                else:
                    counter[fruits[left]] -= 1
                left += 1
        # print(left, right)
        return res