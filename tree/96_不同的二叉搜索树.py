from util.common_imports import *


class Solution:
    def numTrees(self, n: int) -> int:
        D = defaultdict(int)
        D[0] = 1
        D[1] = 1
        D[2] = 2
        # D[3] = 5

        def visit(x):
            if x in D:
                return D[x]
            else:
                ans = 0
                for root in range(x):
                    left = root
                    right = x - 1 - root
                    ans += visit(left) * visit(right)
                D[x] = ans
                return ans

        visit(n)
        return D[n]


# print(Solution().numTrees(3))
print(Solution().numTrees(4))
