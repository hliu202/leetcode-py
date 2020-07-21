# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
from util.common_imports import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def genNode(start, end):
            if start > end:
                return None
            if start == end:
                return [TreeNode(start)]

            ans = []
            for root in range(start, end+1):
                left = genNode(start, root - 1)
                right = genNode(root+1, end)
                if left:
                    for L in left:
                        if right:
                            for R in right:
                                RT = TreeNode(root)
                                RT.left = L
                                RT.right = R
                                ans.append(RT)
                        else:
                            RT = TreeNode(root)
                            RT.left = L
                            ans.append(RT)
                else:
                    for R in right:
                        RT = TreeNode(root)
                        RT.right = R
                        ans.append(RT)

            return ans
        
        return genNode(1, n)

res = Solution().generateTrees(3)
for r in res:
    printTree(r)
    