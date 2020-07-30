class Solution:
    def integerBreak(self, n: int) -> int:
        n3 = n // 3
        left = n % 3
        if n3 > 0:
            if left == 1:
                ans = 4
                n3 -= 1
            elif left == 0:
                if n3 == 1:
                    return 2
                ans = 1
            else:
                ans = left

            while n3:
                ans *= 3
                n3 -= 1
            return ans
        else:
            if left == 2:
                return 1
            return 0


print(Solution().integerBreak(2))
print(Solution().integerBreak(10))
print(Solution().integerBreak(8))
