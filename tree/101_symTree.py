# https://leetcode-cn.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def pre(A, B):
            if not A and not B: return True
            if not A or not B: return False
            if A.val == B.val:
                return pre(A.left, B.right) and pre(A.right, B.left)
        
        if root is None:
            return True
        return pre(root.left, root.right)
    

print(Solution().isSymmetric(createTree([1,2,2,3,4,4,3])))
print(Solution().isSymmetric(createTree([1,2,2,None,3,None,3])))