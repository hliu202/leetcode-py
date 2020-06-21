# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.common_imports import *


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        deq = deque()
        deq.append(root)

        res = "["
        while deq:  # BFS
            cur = deq.popleft()
            res += (str(cur.val) if cur is not None else "null") + ","
            if cur is not None:
                deq.append(cur.left)
                deq.append(cur.right)
        j = len(res) - 2  # ,
        while j > 0 and not res[j].isdigit():
            j -= 1
        return res[0 : j + 1] + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data[1:-1].split(",")
        if not len(vals):
            return None

        deq = deque()
        root = TreeNode(vals[0])
        deq.append(root)
        i, n = 1, len(vals)
        while deq and i < n:
            cur = deq.popleft()
            if vals[i] != "null":
                left = TreeNode(vals[i])
                cur.left = left
                deq.append(left)
            i += 1

            if vals[i] != "null":
                right = TreeNode(vals[i])
                cur.right = right
                deq.append(right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
codec = Codec()
# printTree(codec.deserialize(codec.serialize(createTree([1, 2, 3, None, None, 4, 5]))))
# printTree(codec.deserialize(codec.serialize(None)))
# print(codec.serialize(codec.deserialize("1,2,3,null,null,4,5,null,null,null,null")))
print(codec.serialize(codec.deserialize("[5,4,8,11,null,13,4,7,2,null,null,null,1]")))
print(codec.serialize(codec.deserialize("[]")))
