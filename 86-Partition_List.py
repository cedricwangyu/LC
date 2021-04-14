# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1, head2 = ListNode(0), ListNode(0)
        node1, node2 = head1, head2
        while head:
            if head.val < x: node1.next, node1 = head, head
            else: node2.next, node2 = head, head
            head = head.next
        node1.next, node2.next = head2.next, None
        return head1.next
