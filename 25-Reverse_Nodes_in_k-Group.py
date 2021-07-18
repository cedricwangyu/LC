# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prev, p, node, first = None, [], head, True
        while node:
            p.append(node)
            if len(p) == k:
                Nnode = p[-1].next
                if prev: prev.next = p[-1]
                for i in range(1, k): p[i].next = p[i-1]
                p[0].next, prev, node = Nnode, p[0], p[0]
                if first: head, first = p[-1], False
                p.clear()
                
            node = node.next
        return head
