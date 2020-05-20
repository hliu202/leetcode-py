# https://leetcode-cn.com/problems/min-stack/solution/chai-zhi-fa-155-zui-xiao-zhan-by-fe-lucifer/

from collections import deque

# 差值法
# 1. min, 和 min 的差值 (x - min)
# 2. if cur < 0, cur 是: 当前最小值 - 上一个最小值，即 last_min = cur_min - cur
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.deq = deque()  # faster than list: 132ms vs 172ms
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.deq) == 0:
            self.min = x
            self.deq.append(0)
        else:
            sub = x - self.min
            self.deq.append(sub)
            if sub < 0:
                self.min = x

    def pop(self):
        """
        :rtype: None
        """
        if len(self.deq) == 0:
            return None

        sub = self.deq.pop()
        if sub < 0:
            cur = self.min  # min is current!
            self.min = self.min - sub   # restore last_min
            return cur
        else:
            return sub + self.min
           
    def top(self):
        """
        :rtype: int
        """
        if len(self.deq) == 0:
            return None
        if self.deq[-1] < 0:    # min is current!
            return self.min
        else:
            return self.deq[-1] + self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

ms = MinStack()
ms.push(2147483646)
ms.push(2147483646)
ms.push(2147483647)
print (ms.top())
print (ms.pop())
print (ms.getMin())
print (ms.pop())
print (ms.getMin())
print (ms.pop())
ms.push(2147483647)
print (ms.top())
print (ms.getMin())
ms.push(-2147483648)
print (ms.top())
print (ms.getMin())
print (ms.pop())
print (ms.getMin())
