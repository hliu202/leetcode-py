# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from util.common_imports import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == q.val:
            return p
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val:
            if q.val > root.val:
                return root
            else:
                return self.lowestCommonAncestor(root.left, p, q)
        else:
            if q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root

