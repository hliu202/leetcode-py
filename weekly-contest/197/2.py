from util.common_imports import *
# from collections import *

class Solution:
    def numSub(self, s: str) -> int:
        if not s:
            return 0

        D = defaultdict(int)
        cur = 0
        for c in s:
            if c == "0" and cur > 0:
                D[cur] += 1
                cur = 0
            if c == "1":
                cur += 1
        if s[-1] == "1":
            D[cur] += 1

        ans = 0

        def count(n):
            if n % 2 == 0:
                return (n + 1) * (n // 2)
            else:
                return n + count(n - 1)

        M = 10**9 + 7
        for k in D.keys():
            v = D[k]
            ans += count(k) * v
            ans %= M
        return ans

print(Solution().numSub(s = "0110111"))
print(Solution().numSub(s = "101"))
print(Solution().numSub(s = "111111"))
print(Solution().numSub(s = "000"))