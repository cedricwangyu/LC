# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        if head.next is None:
            return head
        
        node = head.next
        head.next = None

        while(node is not None):
            nextnode = node.next
            node_seen = head
            node_pre = None
            while(node_seen is not None):
                if node_seen.val < node.val:
                    node_pre = node_seen
                    node_seen = node_seen.next
                else:
                    if node_pre is None:
                        head = node
                        node.next = node_seen
                    else:
                        node_pre.next = node
                        node.next = node_seen
                    break
            if node_seen is None:
                node_pre.next = node
                node.next = None
            node = nextnode
        
        return head
            
                
        