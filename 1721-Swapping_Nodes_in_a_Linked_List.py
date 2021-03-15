# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        i, node, knode, nknode = 1, head, None, head
        while node:
            if i == k: knode = node
            if i - k > 0: nknode = nknode.next 
            i += 1
            node = node.next
        knode.val, nknode.val = nknode.val, knode.val
        return head