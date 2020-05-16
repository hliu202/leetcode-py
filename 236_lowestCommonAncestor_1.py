
from util import tree_node
from util.tree_node import TreeNode

# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/

#1. 如果root是p or q: return root
#2. 如果left和right都是None，return None
#3. 如果left和right都不是None，return root（説明是當前節點）
#4. return left和right中的一個
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: # 1
            return root

        rl = self.lowestCommonAncestor(root.left, p, q)
        rr = self.lowestCommonAncestor(root.right, p, q)

        if not rl and not rr: return # 2
        if rl and rr: return root # 3
        if rl: return rl #4
        return rr

root = tree_node.createTree([3,5,1,6,2,0,8,None,None,7,4])
res = Solution().lowestCommonAncestor(root, root.left, root.left.right.right)
print(res.val)
