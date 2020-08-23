# 汉明距离是使用在数据传输差错控制编码里面的，汉明距离是一个概念，它表示两个（相同长度）字对应位不同的数量，我们以d（x,y）表示两个字x,y之间的汉明距离。
# 对两个字符串进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离。

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

        # res = x ^ y
        # res_b = bin(res)
        # ans = 0
        # for c in res_b:
        #     if c == '1':
        #         ans += 1
        # return ans


# print(Solution().hammingDistance(x = 1, y = 4))
print(Solution().hammingDistance(x = 2143896, y = 2233796))
print(Solution().hammingDistance(x = int("1011101", 2), y = int("1001001", 2)))
