class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = list(str(n))
        i = len(a) - 2
        while i >= 0 and a[i] >= a[i+1]:
            i -= 1
        if i < 0:
            return -1
        j = len(a) - 1
        while j >= 0 and a[j] <= a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
        r = a[:i+1] + a[len(a)-1:i:-1]
        res = int(''.join(r))
        return res if res < 2**31-1 else -1