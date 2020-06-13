# https://leetcode-cn.com/problems/climbing-stairs/
# N1: i-1 以 1结尾
# N2: i-1 以 2结尾
# for i: N1 = N2+old.N1, N2 = old.N1
class Solution:
    def climbStairs(self, n: int) -> int:
        N1 = 1
        N2 = 0
        for _ in range(1, n):
            tmp = N1
            N1 += N2
            N2 = tmp
        return N1 + N2


print(Solution().climbStairs(3))
print(Solution().climbStairs(5))
