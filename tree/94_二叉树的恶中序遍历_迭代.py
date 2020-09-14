from util.common_imports import *

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stk = deque()

        if not root: return ans

        cur = root
        while cur:
            stk.append(cur)
            cur = cur.left

        while stk:
            cur = stk.pop()
            ans.append(cur.val)

            if cur.right:
                stk.append(cur.right)
                cur = cur.right.left
                while cur:
                    stk.append(cur)
                    cur = cur.left

        return ans

print(Solution().inorderTraversal(createTree("[1,null,2,3]")))

# 在所有 Python3 提交中击败了 88.72% 的用户
