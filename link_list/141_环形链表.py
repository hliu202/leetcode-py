# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        n1, n2 = head.next, head.next.next
        while n1 and n2 and n1 != n2:
            if not n1.next or not n2.next or not n2.next.next:
                return False
            else:
                n1 = n1.next
                n2 = n2.next.next

        return n1 == n2
        