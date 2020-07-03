# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        n = len(nums)
        mid = n // 2
        cur = TreeNode(nums[mid])
        if mid > 0:
            cur.left = self.sortedArrayToBST(nums[0:mid])
        if mid < n - 1:
            cur.right = self.sortedArrayToBST(nums[mid + 1 :])
        return cur


printTree(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))

