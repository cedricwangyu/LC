# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast.next and fast.next.next: slow, fast = slow.next, fast.next.next
        if fast.next: slow = slow.next
        return slow
