# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if prev: prev.next, curr = curr.next, curr.next
                else: head, curr = curr.next, curr.next
            else: curr, prev = curr.next, curr
        return head
