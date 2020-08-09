from util.common_imports import *


class Solution:
    def isBST(self, root: TreeNode) -> None:
        valid = True

        def dfs(node):
            nonlocal valid

            if node.left:
                min_l, max_l = dfs(node.left)
                if not valid:
                    return 0, 0

                if max_l > node.val:
                    valid = False
                    return 0, 0
                min_cur = min_l
            else:
                min_cur = node.val

            if node.right:
                min_r, max_r = dfs(node.right)
                if not valid:
                    return 0, 0

                if min_r < node.val:
                    valid = False
                    return 0, 0
                max_cur = max_r
            else:
                max_cur = node.val
            return min_cur, max_cur

        dfs(root)
        return valid


print(Solution().isBST(createTree("[1,3,null,null,2]")))
print(Solution().isBST(createTree("[3,1,4,null,null,2]")))
