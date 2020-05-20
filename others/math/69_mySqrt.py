# https://leetcode-cn.com/problems/sqrtx/

class Solution:

    def mySqrt(self, x):
        if x == 0:
            return 0

        mid = x >> 1
        upper = x
        while True:
            cur = mid * mid
            if cur == x:
                return mid
            elif cur < x: # too small
                if cur + 2*mid + 1 > x:  # mid * mid < x AND (mid + 1) * (mid + 1) > x
                    return mid
                else:
                    mid = (mid + upper + 1) >> 1    # infinite loop!
            else: # too large
                upper = mid
                mid = mid >> 1

print(Solution().mySqrt(129))
print(Solution().mySqrt(1))

# https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
