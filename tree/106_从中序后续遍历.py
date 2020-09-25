# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return None

        cur = TreeNode(postorder[-1])
        if len(inorder) == 1: return cur

        # root split inorder: left and right
        idx = inorder.index(postorder[-1])
        
        # cur val should not be included
        left_in = inorder[0:idx]
        right_in = inorder[idx+1:]

        ll = len(left_in)
        left_post = postorder[0:ll]
        right_post = postorder[ll:-1]
        cur.left = self.buildTree(left_in, left_post)
        cur.right = self.buildTree(right_in, right_post)
        return cur

printTree(Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))            
printTree(Solution().buildTree(inorder = [2,3,1], postorder = [3,2,1]))            
printTree(Solution().buildTree(inorder = [1,2,3], postorder = [3,2,1]))            

