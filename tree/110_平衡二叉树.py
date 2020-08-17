# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        isValid = True
        def dfs(node):
            nonlocal isValid
            if not node: return 0
            hl = dfs(node.left)
            hr = dfs(node.right)
            if hl > hr:
                if hl - hr > 1:
                    isValid = False
                return hl + 1
            else:
                if hr - hl > 1:
                    isValid = False
                return hr + 1
        dfs(root)
        return isValid


print(Solution().isBalanced(createTree("[1,2,2,3,3,null,null,4,4]")))


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1 # invalid height
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
