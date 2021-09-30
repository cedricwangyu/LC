# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node, n, res = head, 0, [] * k
        while node is not None: node, n = node.next, n+1
        m = n - n // k * k
        node, curr_l, curr_m, l = head, 0, 0, n // k + int(m > 0)
        while node is not None:
            curr_l += 1
            if curr_l == 1: res.append(node)
            if curr_l == l:
                nextnode = node.next
                node.next = None
                curr_l = 0
                curr_m += 1
                if curr_m == m: l -= 1
                node = nextnode
            else:
                node = node.next
        while len(res) < k: res.append(None)
        return res
