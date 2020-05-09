# https://leetcode-cn.com/problems/sqrtx/

# 牛顿迭代法
# 求出根号 a 的近似值：
#  1 首先随便猜一个近似值 x，
#  2 然后不断令 x 等于 x 和 a/x 的平均数，
#  3 迭代个六七次后 x 的值就已经相当精确了。
class Solution:

    def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

print(Solution().mySqrt(128))
