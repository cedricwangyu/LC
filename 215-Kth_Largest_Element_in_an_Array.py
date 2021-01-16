class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def inserttowindow(window, num):
            if num >= window[-1]: 
                window.pop(0)
                window.append(num)
            elif num <= window[0]: return
            else:
                left, right = 0, len(window) - 1
                while right - left > 1:
                    mid = (left + right) // 2
                    if window[mid] == num:
                        window.insert(mid, num)
                        window.pop(0)
                        return
                    elif window[mid] > num: right = mid
                    else: left = mid
                window.insert(right, num)
                window.pop(0)
        
        if k <= len(nums) // 2:
            window = sorted(nums[:k])
            for i in nums[k:]: inserttowindow(window, i)
            return window[0]
        else:
            k = len(nums) - k + 1
            window = sorted([-item for item in nums[:k]])
            for i in [-item for item in nums[k:]]: inserttowindow(window, i)
            return - window[0]