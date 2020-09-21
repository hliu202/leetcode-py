# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def dfs(node, add_val):
            if not node: return node

            if node.right:
                add_val = dfs(node.right, add_val)
            add_val += node.val
            node.val = add_val
            if node.left:
                add_val = dfs(node.left, add_val)
            return add_val

        dfs(root, 0)
        return root

printTree(Solution().convertBST(createTree("[5,2,13]")))
