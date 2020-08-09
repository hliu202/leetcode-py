# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from util.common_imports import *


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        done = False

        def change(node, val, toVal):
            if node and node.val == val:
                node.val = toVal
                return

            self.change(node.left, val, toVal)
            self.change(node.left, val, toVal)

        def dfs(node):
            nonlocal done

            if node.left:
                min_l, max_l = dfs(node.left)
                if not done and max_l > node.val:
                    node.val, tmp = max_l, node.val
                    change(node.left, max_l, tmp)
                    done = True
                    return 0, 0
            if node.right:
                min_r, max_r = dfs(node.right)
                if not done and min_r < node.val:
                    node.val, tmp = min_r, node.val
                    change(node.right, min_r, tmp)
                    done = True
                    return 0, 0
            return min_l if node.left else node.val, max_r if node.right else node.val

        dfs(root)
        return root


print(serialize(Solution().recoverTree(createTree("[1,3,null,null,2]"))))
# print(serialize(Solution().recoverTree(createTree("[3,1,4,null,null,2]"))))
