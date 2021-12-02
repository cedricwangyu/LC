# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head, even_head =  ListNode(), ListNode()
        odd, even, node, i = odd_head, even_head, head, 1
        while node:
            if i % 2 == 1: 
                odd.next = node
                odd = odd.next
            else: 
                even.next = node
                even = even.next
            node, i = node.next, i+1
        odd.next, even.next = even_head.next, None
        return odd_head.next
