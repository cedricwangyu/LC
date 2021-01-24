# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def bisect_insert(self, lists, node):
        if node.val >= lists[-1].val: lists.append(node)
        elif node.val <= lists[0].val: lists.insert(0, node)
        else:
            left, right = 0, len(lists) - 1
            while(right - left > 1):
                mid = (left + right) // 2
                if lists[mid].val == node.val:
                    lists.insert(mid, node)
                    return
                elif lists[mid].val > node.val: right = mid
                else: left = mid
            lists.insert(right, node)
            
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [item for item in lists if item]
        if len(lists) <= 0: return
        if len(lists) == 1: return lists[0]
        lists.sort(key = lambda x: x.val)
        head = ListNode()
        node = head
        while(len(lists) > 0):
            node.next = lists.pop(0)
            node = node.next
            if node.next:
                if len(lists) <= 0: lists.append(node.next)
                else: self.bisect_insert(lists, node.next)
        return head.next
            
            
            
        