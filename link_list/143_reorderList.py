# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.common_imports import *


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        deq = deque()
        cur = head
        count = 0
        while cur:
            deq.append(cur)
            cur = cur.next
            count += 1

        cur = head
        tail = deq.pop()

        is_even = False
        if count % 2 == 0:
            is_even = True

        count //= 2
        while count > 0:
            tmp = cur.next
            cur.next = tail
            tail.next = tmp

            count -= 1
            if count == 0:  # last
                if is_even:
                    tail.next = None
                else:
                    tmp.next = None
                break

            cur = tmp
            tail = deq.pop()

        return head


printLinkedList(Solution().reorderList(createLinkedList([1, 2, 3, 4])))
printLinkedList(Solution().reorderList(createLinkedList([1, 2, 3, 4, 5])))
