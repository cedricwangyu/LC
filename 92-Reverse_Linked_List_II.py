# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, m, n):
        if not head: return None
        self.left, right, self.stop = head, head, False
        def recurseAndReverse(right, m, n):
            if n == 1: return
            right = right.next
            if m > 1: self.left = self.left.next
            recurseAndReverse(right, m - 1, n - 1)
            if self.left == right or right.next == self.left: self.stop = True    
            if not self.stop:
                self.left.val, right.val = right.val, self.left.val
                self.left = self.left.next           
        recurseAndReverse(right, m, n)
        return head
