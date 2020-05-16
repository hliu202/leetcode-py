# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# !! 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

import collections
from util.list_node import *

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        q = collections.deque()
        cur = head
        head = None
        Pre = None
        nK0 = None
        while cur:
            count = 0
            while count < k and cur:
                q.append(cur)
                cur = cur.next
                count += 1

            if count == k:
                if head is None:
                    head = q[-1]
                nK0 = q[-1].next  # !! 别在循环里面判断 nK0 = None => infinite loop

                while q:
                    cur = q.pop()
                    if Pre: # head
                        Pre.next = cur
                    Pre = cur
                    
                cur.next = None # last
                cur = nK0
                nK0 = None
            else:
                if Pre:
                    Pre.next = q.popleft()
                break
        
        return head

# printLinkedList( 
#     Solution().reverseKGroup(
#         createLinkedList([1,2,3,4,5]), 
#         2))

printLinkedList( 
    Solution().reverseKGroup(
        createLinkedList([1,2,3,4,5]), 
        3))
