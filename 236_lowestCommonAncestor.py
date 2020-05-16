
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

from util import tree_node
from util.tree_node import TreeNode

res = None
xp = None
xq = None

def dfs(N:TreeNode):
    global res, xp, xq
    if not N:
        return False
    
    if res is None:
        isL = dfs(N.left)
        isR = dfs(N.right)

        if isL and isR:
            res = N
        elif N == xp or N == xq:
            if isL or isR:
                res = N
            return True
        else:
            return isL or isR
    return False

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        global xp, xq
        xp = p
        xq = q
        dfs(root)
        return res


root = tree_node.createTree([3,5,1,6,2,0,8,None,None,7,4])
res = Solution().lowestCommonAncestor(root, root.left, root.left.right.right)
print(res.val)
