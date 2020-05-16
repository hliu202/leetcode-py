
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(A):
    if not A: 
        return None

    head = pre = ListNode(A[0])
    for i in range(1, len(A)):
        cur = ListNode(A[i])
        pre.next = cur
        pre = cur
    return head

def printLinkedList(A):
    print('[', end='')
    while A:
        if A.next: print(A.val, end=', ')
        else: print(A.val, end='')
        A = A.next
    print(']')
# head = createLinkedList([1, 2, 3, 4, 5])
# print (head)
