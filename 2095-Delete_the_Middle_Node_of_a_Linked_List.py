# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        middle_node, prev_middle_node, curr_node = head.next, head, head.next
        while curr_node.next is not None and curr_node.next.next is not None:
            curr_node, middle_node, prev_middle_node = curr_node.next.next, middle_node.next, prev_middle_node.next
        
        prev_middle_node.next = middle_node.next
        return head
            