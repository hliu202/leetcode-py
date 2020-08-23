class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/shu-zi-fan-wei-an-wei-yu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 「Brian Kernighan 算法」清除二进制串中最右边的 1。
# ! 布赖恩·克尼根: 
# 1. 是否可以像人类直观的计数比特为 1 的位数，跳过两个 1 之间的 0。例如：10001000。
# 2. 抹去'最右'边的 1
# while x:
#   x = x & (x-1)
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n
