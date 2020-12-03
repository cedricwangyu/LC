# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        node = head
        self.head = head
        self.n = 1
        while (node.next is not None):
            self.n += 1
            node = node.next
        
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        i = random.randint(0, self.n - 1)
        node = self.head
        for j in range(i):
            node = node.next
        
        return node.val
            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()