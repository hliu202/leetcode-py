# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *


class Solution:
    def rob(self, root: TreeNode) -> int:
        def visit(node):  # 返回 1)包含根节点, 2)不包含根节点
            if not node:
                return (0, 0)

            vl0, vl1 = visit(node.left)
            vr0, vr1 = visit(node.right)
            #!4 种不包含根节点的情况
            return vl1 + vr1 + node.val, max(vl0 + vr0, vl1 + vr1, vr0 + vl1, vl0 + vr1)

        v0, v1 = visit(root)
        return max(v0, v1)


# print(Solution().rob(createTree("[3,2,3,null,3,null,1]")))
# print(Solution().rob(createTree("[3,4,5,1,3,null,1]")))
# print(Solution().rob(createTree("[4,1,null,2,null,3]"))) # 7
#    4
#   1
#  2
# 3

print(Solution().rob(createTree("[2,1,3,null,4]")))  # 7
#  2
# 1 3
# 4
