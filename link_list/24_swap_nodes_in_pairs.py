# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head

        if not head.next: return head

        nhead = head.next
        head.next = self.swapPairs(head.next.next)
        nhead.next = head
        return nhead
