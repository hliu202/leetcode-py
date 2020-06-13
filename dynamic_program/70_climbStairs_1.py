# https://leetcode-cn.com/problems/climbing-stairs/
# f(i) = f(i-1) + f(i-2)


class Solution:
    def climbStairs(self, n: int) -> int:
        f0, f1, f2 = 0, 0, 1
        for _ in range(1, n + 1):
            # tmp = f2
            f0 = f1
            f1 = f2
            f2 = f0 + f1
        return f2


print(Solution().climbStairs(3))
print(Solution().climbStairs(5))

