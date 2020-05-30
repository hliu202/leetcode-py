# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
from util.common_imports import *

# mono stack 单调栈： 2次遍历，找出左/右两边的“比当前 height[i] 小的边界点”，而不用 O(n^2)分别对每个 i 找左右边界


class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        n = len(A)
        left, right = [0]*n, [0]*n
        mono_stack = deque()

        for i in range(n):
            while mono_stack and A[mono_stack[-1]] >= A[i]:
                mono_stack.pop()

            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = deque()
        for i in range(n-1, -1, -1):
            while mono_stack and A[mono_stack[-1]] >= A[i]:
                mono_stack.pop()

            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        res = max(A[i] * (right[i] - left[i] - 1)
                  for i in range(n)) if n > 0 else 0
        return res


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([4, 2]))
print(Solution().largestRectangleArea([2, 1, 2]))

