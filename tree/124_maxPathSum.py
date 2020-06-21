# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, node.val + left + right)
            return max(0, node.val + left, node.val + right)

        dfs(root)
        return self.res


# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         self.maxsum = float('-inf')
#         def dfs(root):
#             if not root: return 0
#             left = dfs(root.left)
#             right = dfs(root.right)
#             self.maxsum = max(self.maxsum, left + right + root.val)
#             return max(0, max(left, right) + root.val)
#         print(dfs(root))
#         return self.maxsum

# print (Solution().maxPathSum(createTree([1,2,3])))
# print (Solution().maxPathSum(createTree([-10,9,20,None,None,15,7])))
print(
    Solution().maxPathSum(createTree("[5,4,8,11,null,13,4,7,2,null,null,null,1]"))
)  # 48
