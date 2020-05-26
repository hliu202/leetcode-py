# https://leetcode-cn.com/problems/linked-list-cycle-ii/
from util import list_node

# Floyd 算法

class Solution:
    def hasCycle(self, head: ListNode) -> ListNode:
        slow = head
        quick = head
        if head is None:
            return None
        while True:
            if quick.next is None:
                return None
            quick = quick.next
            
            if quick.next is None:
                return None
            quick = quick.next
            
            slow = slow.next
            if quick == slow:
                return slow
        
    def detectCycle(self, head: ListNode) -> ListNode:
        meet = self.hasCycle(head)
        if meet is None:
            return None
        
        ptr2 = meet
        ptr1 = head

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1

