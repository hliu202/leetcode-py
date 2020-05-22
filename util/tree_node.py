
# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createNode(A, idxOfLevel, depth):
    idx = (1<<depth) - 1 + idxOfLevel
    if idx < len(A) and A[idx] is not None:
        tn = TreeNode(A[idx])

        tn.left = createNode(A, idxOfLevel*2, depth+1)
        tn.right = createNode(A, idxOfLevel*2+1, depth+1)
        return tn

    return None

def createTree(A):
    return createNode(A, 0, 0)

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

def printTree(root :TreeNode):
    res = levelOrder(root)
    for L in res:
        print (L)
