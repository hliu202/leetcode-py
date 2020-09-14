from util.common_imports import *

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def inorder(node):
            nonlocal ans

            if not node: return

            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans

print(Solution().inorderTraversal(createTree("[1,null,2,3]")))
