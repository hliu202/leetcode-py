# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
# sys.path.append('../')
# sys.path.insert(1, '/Users/hao/dev/leetcode-py')
from util.tree_node import *
from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # root = preorder[0]
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root =TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[0:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root

# printTree(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))
printTree(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))
