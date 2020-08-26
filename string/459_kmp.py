# https://leetcode-cn.com/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(query: str, pattern: str) -> bool:
            n, m = len(query), len(pattern)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            match = -1
            for i in range(1, n - 1):
                while match != -1 and pattern[match + 1] != query[i]:
                    match = fail[match]
                if pattern[match + 1] == query[i]:
                    match += 1
                    if match == m - 1:
                        return True
            return False
        
        return kmp(s + s, s)


print(Solution().repeatedSubstringPattern("abac"))                    
# print(Solution().repeatedSubstringPattern("abab"))                    
# print(Solution().repeatedSubstringPattern("aba"))                    
# print(Solution().repeatedSubstringPattern("bb"))                    
# print(Solution().repeatedSubstringPattern("abcabcabcabc"))   

# 「在模 n 的意义下」可以理解为，所有的加法运算的结果都需要对 n 取模，使得结果保持在 [0, n) 中，这样加法就自带了「旋转」的效果。
# gcd(n,i) 最大公约数 gcd(8,4) = 4, gcd(6, 9) = 3