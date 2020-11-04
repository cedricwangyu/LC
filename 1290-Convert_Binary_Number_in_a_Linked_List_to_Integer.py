# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head.next:
            res = 2 * res + head.val
            head = head.next
            
        res = 2 * res + head.val
        # print(res)
        return res
        