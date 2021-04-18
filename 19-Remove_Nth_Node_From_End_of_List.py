# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i, curr, prev_tar = 1, head, ListNode(val=-1, next=head)
        while curr.next:
            i, curr = i+1, curr.next
            if i > n: prev_tar = prev_tar.next
        if i == n: return head.next
        elif i > n: prev_tar.next = prev_tar.next.next
        return head
