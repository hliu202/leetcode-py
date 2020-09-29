# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.common_imports import *

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node):
            nonlocal ans
            if not node: return

            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans

print(Solution().postorderTraversal(createTree("[1,null,2,3]")))
