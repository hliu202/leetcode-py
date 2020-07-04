# https://leetcode-cn.com/problems/longest-valid-parentheses/

# f(i)有多少以i为结尾有多少个连续空格
# stack_leftP 保存空余'('
from util.common_imports import *


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        left_p = deque()
        f = [0] * (len(s) + 1) # f[0]哨兵
        for i in range(len(s)):
            if s[i] == "(":
                left_p.append(i)
            elif left_p:
                l_idx = left_p.pop()
                f[i + 1] = f[i] + 2 + f[l_idx]
                ans = max(ans, f[i + 1])

        return ans


print(Solution().longestValidParentheses("(()"))
print(Solution().longestValidParentheses(")()())"))
