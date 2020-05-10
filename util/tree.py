
# Definition for a binary tree node.
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
