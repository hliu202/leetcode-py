from util.common_imports import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def dfs(node):
            if node.left is None and node.right is None:
                return [0] # leaf
            ld,rd = None, None
            if node.left:
                ld = dfs(node.left)
            if node.right:
                rd = dfs(node.right)
            if ld:
                for i in range(len(ld)):
                    ld[i] += 1
            if rd:
                for i in range(len(rd)):
                    rd[i] += 1

            if ld and rd:
                for ll in ld:
                    for rr in rd:
                        if ll + rr <= distance:
                            self.ans += 1
                ld.extend(rd)
                return ld
            if ld:
                return ld
            if rd:
                return rd

        dfs(root)
        return self.ans

# print(Solution().countPairs(createTree('[1,2,3,null,4]'), 3))
# print(Solution().countPairs(createTree('[1,2,3,4,5,6,7]'), 3))
# print(Solution().countPairs(createTree('[7,1,4,6,null,5,3,null,null,null,null,null,2]'), 3))
print(Solution().countPairs(createTree('[100]'), 1))
print(Solution().countPairs(createTree('[1,1,1]'), 2))
