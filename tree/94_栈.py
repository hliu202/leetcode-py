class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res, cur = [], [], root
        while cur or stack:  # 混合进出栈的时候，可以使用这样的判断
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                this = stack.pop()
                res.append(this.val)
                cur = this.right
        return res
