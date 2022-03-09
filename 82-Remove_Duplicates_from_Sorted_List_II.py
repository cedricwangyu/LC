# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum_head = ListNode(val = float('-Inf'), next=None)
        last, prev, curr, res = dum_head, dum_head, head, dum_head
        while curr:
            if curr.val > prev.val:
                if not curr.next or (curr.next.val > curr.val):
                    last.next = curr
                    last = curr
            prev = curr
            curr = curr.next
        last.next = None
        return res.next
                    
                
            