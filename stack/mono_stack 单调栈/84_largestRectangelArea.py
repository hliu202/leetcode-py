# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
from util.common_imports import *
class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0

        res = A[0]
        for i in range(len(A)):
            if i == 0:
                j = i + 1
                while j < len(A) and A[j] >= A[i]: # find A[j] < A[i] and stop
                    j += 1

                cur = A[i] * (j - i) # A[i]为宽的矩形
                res = max(res, cur)
                continue

            if A[i] < A[i-1]:
                j = i + 1
                while j < len(A) and A[j] >= A[i]: # find A[j] < A[i] and stop
                    j += 1
                k = i - 1
                while k >= 0 and A[k] >= A[i]: # find A[k] < A[i] and stop
                    k -= 1
                cur = A[i] * (j - (k + 1))
                res = max(res, cur)
            elif A[i] > A[i-1]:
                j = i + 1
                while j < len(A) and A[j] >= A[i]: # find A[j] < A[i] and stop
                    j += 1

                cur = A[i] * (j - i) # A[i]为宽的矩形
                res = max(res, cur)
        return res

# print (Solution().largestRectangleArea([2,1,5,6,2,3]))
# print (Solution().largestRectangleArea([4,2]))
print (Solution().largestRectangleArea([2,1,2]))

# 超出时间限制