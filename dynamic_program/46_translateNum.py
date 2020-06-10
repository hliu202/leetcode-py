
# N1：i-1单独的个数
# N2：i-1是连词的个数
class Solution:
    def translateNum(self, num: int) -> int:
        n = str(num)
        N1 = 1
        N2 = 0
        for i in range(1,len(n)):
            tmp = N2
            if (n[i-1] == '2' and n[i] <= '5') or n[i-1] == '1': # 可以连接
                N2 = N1 # n[i-1]n[i]组合
            else:
                N2 = 0
            N1 += tmp
        
        return N1 + N2

# print (Solution().translateNum(12258))
print (Solution().translateNum(18580))