class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        L = [(start + i*2) for i in range(n)]
        # print (L)

        res = 0
        for v in L:
            res ^= v
        return res
print (Solution().xorOperation(5, 0))
print (Solution().xorOperation(4, 3))
print (Solution().xorOperation(1, 7))
print (Solution().xorOperation(10, 5))