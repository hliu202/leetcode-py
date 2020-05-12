# https://leetcode-cn.com/problems/min-stack/

from collections import deque

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.deq = deque()
        self.minq = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.deq.append(x)

        if len(self.minq) == 0 or self.minq[-1][0] > x:  # record min and location
            self.minq.append((x, len(self.deq)))   

    def pop(self):
        """
        :rtype: None
        """
        if len(self.deq) == 0:
            return None

        if self.minq[-1][1] == len(self.deq):
            self.minq.pop()

        return self.deq.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.deq) == 0:
            return None
        return self.deq[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minq[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print (minStack.getMin())
print (minStack.pop())
print (minStack.top())
print (minStack.getMin())
