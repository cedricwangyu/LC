# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None: return False
        fast, slow = head, head
        while(fast.next is not None and fast.next.next is not None and slow.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val: return True
        
        return False