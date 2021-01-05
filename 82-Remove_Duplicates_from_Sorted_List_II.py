# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None: return head
        blacklist, L, R = set(), head, head.next
        while R:
            if L.val == R.val: blacklist.add(L.val)
            L, R = L.next, R.next
        L, R = ListNode(-101), head
        head = L
        while R:
            if R.val in blacklist: R = R.next
            else: L.next, L, R = R, R, R.next
        L.next = R
        return head.next
        
        