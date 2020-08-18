# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = vall
#         self.left = left
#         self.right = right
from util.common_imports import *


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None

        L = []
        n = head
        while n:
            L.append(n.val)
            n = n.next

        def toBST(start, end):
            if start > end: return None

            mid = (start + end) // 2
            tn = TreeNode(L[mid])
            tn.left = toBST(start, mid - 1)
            tn.right = toBST(mid+1, end)
            return tn
        
        return toBST(0, len(L) - 1)

printTree(Solution().sortedListToBST(createLinkedList([-10, -3, 0, 5, 9])))
