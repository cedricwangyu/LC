# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1
        num1 = 0
        while l1:
            num1 = num1*10 + l1.val
            l1 = l1.next
            
        num2 = 0
        while l2:
            num2 = num2*10 + l2.val
            l2 = l2.next
        
        num = str(num1 + num2)
        node = None
        for strint in num[::-1]:
            node = ListNode(val = int(strint), next = node)
        
        return node    
        
        