from util.common_imports import *

# 卡特兰数
# https://baike.baidu.com/item/catalan/7605685?fr=aladdin
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) / (i + 2)
        return int(C)


# print(Solution().numTrees(3))
print(Solution().numTrees(4))
