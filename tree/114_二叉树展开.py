# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

# !结果仍然要是二叉树, 左子树为空

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.common_imports import *


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preList = []

        def preOrder(root):
            if not root:
                return

            preList.append(root)
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        size = len(preList)
        for i in range(1, size):
            prev, curr = preList[i - 1], preList[i]
            prev.left = None
            prev.right = curr

