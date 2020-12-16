# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        num = head.val
        node = head
        while node.next is not None:
            node = node.next
            num = num * 10 + node.val
        num += 1
        if num % 10 == 0:
            if len(str(num)) > len(str(num - 1)): node.next = ListNode()
            node = head
            for n in [int(i) for i in str(num)]:
                node.val = n
                node = node.next
        else:
            node.val += 1

        return head
            