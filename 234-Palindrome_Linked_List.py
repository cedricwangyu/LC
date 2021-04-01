# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p = []
        while head: 
            p.append(head.val)
            head = head.next
        return all(p[i] == p[len(p) - i - 1] for i in range(len(p) // 2 + 1))