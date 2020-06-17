# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Like BFS search order

from util.tree_node import *


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        deq = deque()
        deq.append(root)
        results = []
        while deq:
            count = len(deq)
            cur_level = []
            results.append(cur_level)
            while count != 0:
                cur = deq.popleft()
                count -= 1
                cur_level.append(cur.val)

                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)

        return results


print(Solution().levelOrder(createTree([3, 9, 20, None, None, 15, 7])))

