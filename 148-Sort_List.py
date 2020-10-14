# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        n = 0
        node = head
        while(node is not None):
            n += 1
            node = node.next
        node = head
        def dnc(node, n):
            if n <= 1:
                return node
            else:
                nm = int((n - 1)/2)
                node1 = node
                node2 = node
                for i in range(nm):
                    node2 = node2.next
                tnode = node2.next
                node2.next = None
                
                node1 = dnc(node1, nm + 1)
                node2 = dnc(tnode, n - nm - 1)
                
                
                start = True
                snode = node1
                while node1 is not None and node2 is not None:
                    if node1.val >= node2.val:
                        node1, node2 = node2, node1
                    if start:
                        snode = node1
                        start = False
                    if node1.next is not None and node2.val >= node1.next.val:
                        node1 = node1.next
                        node1, node2 = node2, node1
                    else:
                        tnode = node1.next
                        node1.next = node2
                        node1 = tnode
                    
                    
                return snode
        
        return dnc(node, n)
                    
                    
        
        
            