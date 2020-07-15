from functools import lru_cache

# functools.lru_cache装饰器详解 https://blog.csdn.net/u012745215/article/details/78506022

class Solution:
    @lru_cache()
    def numTrees(self, n: int) -> int:
        if n <= 0: return 1
        if n <= 2: return n

        return sum([self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n + 1)])

# 作者：dz-lee
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/di-gui-huan-cun-yi-li-jie-python3-by-dz-lee/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。