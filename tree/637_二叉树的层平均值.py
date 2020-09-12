# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        dq = deque()
        if not root:
            return ans

        dq.append(root)
        while dq:
            cur = len(dq)
            total = 0
            i = 0

            while i < cur:
                node = dq.popleft()
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)

                total += node.val
                i += 1

            ans.append(total/cur)

        return ans

print(Solution().averageOfLevels(createTree("[3,9,20,null,null,15,7]")))
