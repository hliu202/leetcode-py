# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur = deque()
        ans = []
        cur.append(root)
        while cur:
            next = deque()
            cur_ans = []
            while cur:
                node = cur.popleft()
                cur_ans.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            ans.append(cur_ans)
            cur = next
        return ans[::-1]


print(Solution().levelOrderBottom(createTree('[3,9,20,null,null,15,7]')))

# !只用一個queue
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         levelOrder = list()
#         if not root:
#             return levelOrder
        
#         q = collections.deque([root])
#         while q:
#             level = list()
#             size = len(q)
#             for _ in range(size):
#                 node = q.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             levelOrder.append(level)

#         return levelOrder[::-1]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/solution/er-cha-shu-de-ceng-ci-bian-li-ii-by-leetcode-solut/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。