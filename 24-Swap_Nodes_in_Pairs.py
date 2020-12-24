# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node, prev = head, None
        if head is None: return None
        if head.next: head = head.next
        else: return head
        while node is not None:
            if node.next:
                if prev: prev.next = node.next
                node.next.next, node.next, prev = node, node.next.next, node
            node = node.next
        return head