# https://leetcode-cn.com/problems/powx-n/submissions/
class Solution(object):
    def powAbs(self, x, n):
        if n == 0: return 1
        if n & 1 == 0: # even
            rb = self.powAbs(x, n>>1)
            return rb*rb
        else:
            rb = self.powAbs(x, n-1)
            return rb * x

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = self.powAbs(x, abs(n))
        if n < 0:
            return 1/res
        else:
            return res


print (Solution().myPow(2.10000, 3))
print (Solution().myPow(2.10000, 3))