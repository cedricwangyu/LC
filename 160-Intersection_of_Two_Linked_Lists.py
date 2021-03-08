# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB, node = 0, 0, headA
        while node:
            lenA += 1
            node = node.next
        node = headB
        while node:
            lenB += 1
            node = node.next
        while lenA < lenB:
            headB = headB.next
            lenB -= 1
        while lenB < lenA:
            headA = headA.next
            lenA -= 1
        while headA:
            if headA == headB: return headA
            headA = headA.next
            headB = headB.next