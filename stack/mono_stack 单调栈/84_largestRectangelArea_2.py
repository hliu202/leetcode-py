# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
from util.common_imports import *

# mono stack 单调栈： 1次遍历，找出左/右两边的“比当前 height[i] 小的边界点”，而不用 O(n^2)分别对每个 i 找左右边界

# 等等，我们需要的是「一根柱子的左侧且最近的小于其高度的柱子」，但这里我们求的是小于等于
# 如果有若干个柱子的高度都等于矩形的高度，那么最右侧的那根柱子是可以求出正确的右边界的

class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        n = len(A)
        left, right = [0]*n, [n]*n
        mono_stack = deque()

        for i in range(n):
            while mono_stack and A[mono_stack[-1]] >= A[i]:
                right[mono_stack[-1]] = i # ms[-1] 右侧“小于等于”的边界为 i
                mono_stack.pop()

            left[i] = mono_stack[-1] if mono_stack else -1 # i 左侧的“小于”边界
            mono_stack.append(i)

        res = max(A[i] * (right[i] - left[i] - 1)
                  for i in range(n)) if n > 0 else 0
        return res


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([4, 2]))
print(Solution().largestRectangleArea([2, 1, 2]))

