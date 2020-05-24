# https://leetcode-cn.com/contest/weekly-contest-190/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from util.tree_node import *
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        M = defaultdict(int)
        if root is None:
            return 0
        res = 0

        def dfs(n):
            M[n.val] += 1
            nonlocal res
            if n.left == None and n.right == None:
                #leaf
                count = 0
                for v in M.values():
                    if v & 1 == 0:
                        continue
                    else:
                        count += 1
                        if count > 1:
                            # no
                            M[n.val] -= 1
                            return
                res += 1 # found 1
                M[n.val] -= 1
            else:
                if n.left != None:
                    dfs(n.left)
                if n.right != None:
                    dfs(n.right)
                M[n.val] -= 1
        
        dfs(root)
        return res

print(Solution().pseudoPalindromicPaths(createTree([2,3,1,3,1,None,1])))
print(Solution().pseudoPalindromicPaths(createTree([2,1,1,1,3,None,None,None,None,None,1])))
print(Solution().pseudoPalindromicPaths(createTree([9])))