# https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *


class Solution:
    def dfs(self, S, lev, idx):
        i = idx + 1
        while i < len(S) and S[i] != "-":
            i += 1
        cur_val = int(S[idx:i])
        node = TreeNode(cur_val)

        count = 0
        while i < len(S) and S[i] == "-":
            count += 1
            i += 1
        if count == lev + 1:  # left
            left, next_idx, next_count = self.dfs(S, lev + 1, i)
            node.left = left
            if next_count == lev + 1:  # right
                right, next_idx, next_count = self.dfs(S, lev + 1, next_idx)
                node.right = right
            return node, next_idx, next_count
        else:
            return node, i, count

    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        root, _, _ = self.dfs(S, 0, 0)
        return root


printTree(Solution().recoverFromPreorder("1-2--3--4-5--6--7"))
printTree(Solution().recoverFromPreorder("1-2--3---4-5--6---7"))
printTree(Solution().recoverFromPreorder("1-401--349---90--88"))
