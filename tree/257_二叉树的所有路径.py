# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []

        ans = []
        def dfs(pre, node):
            nonlocal ans

            pre += '->' + str(node.val)
            if not node.left and not node.right: # leaf
                ans.append(pre[2:])

            if node.left:
                dfs(pre, node.left)
            if node.right:
                dfs(pre, node.right)
        
        dfs('', root)
        return ans

print(Solution().binaryTreePaths(createTree('[3,9,20,null,null,15,7]')))
