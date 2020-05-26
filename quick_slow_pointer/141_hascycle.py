# https://leetcode-cn.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util import list_node

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        quick = head
        if head is None:
            return False
        while True:
            if quick.next is None:
                return False
            quick = quick.next
            if quick == slow:
                return True
            
            if quick.next is None:
                return False
            quick = quick.next
            if quick == slow:
                return True
            
            slow = slow.next
            if quick == slow:
                return True
        

