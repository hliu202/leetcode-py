# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createNode(A, idxOfLevel, depth):
    idx = (1 << depth) - 1 + idxOfLevel
    if idx < len(A) and A[idx] is not None:
        tn = TreeNode(A[idx])

        tn.left = createNode(A, idxOfLevel * 2, depth + 1)
        tn.right = createNode(A, idxOfLevel * 2 + 1, depth + 1)
        return tn

    return None

def serialize(root: TreeNode):
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
    
def deserialize(data: str):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    vals = data[1:-1].split(",")
    if not len(vals):
        return None

    deq = deque()
    root = TreeNode(int(vals[0]))
    deq.append(root)
    i, n = 1, len(vals)
    while deq and i < n:
        cur = deq.popleft()
        if vals[i] != "null":
            left = TreeNode(int(vals[i]))
            cur.left = left
            deq.append(left)
        i += 1

        if i < n and vals[i] != "null": # 以防最后一个节点,没有右节点
            right = TreeNode(int(vals[i]))
            cur.right = right
            deq.append(right)
        i += 1

    return root


def createTree(A: List):
    return createNode(A, 0, 0)


def createTree(A: str):
    return deserialize(A)


def levelOrder(root):
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


def printTree(root: TreeNode):
    res = levelOrder(root)
    for L in res:
        print(L)
