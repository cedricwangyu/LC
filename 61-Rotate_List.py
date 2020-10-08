# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        
        curr_node = head
        i = 0
        while(curr_node.next != None):
            curr_node = curr_node.next
            i += 1
            
        L = i + 1
        curr_node.next = head
        for i in range(((L - k) % L)):
            curr_node = curr_node.next
        
        new_head = curr_node.next
        curr_node.next = None
        return new_head
        