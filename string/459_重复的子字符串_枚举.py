
from util.common_imports import *

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)

        def check(i):
            np = N // i
            for j in range(0, i):
                for k in range(1, np):
                    if s[j] != s[k*i + j]:
                        return False
            return True

        for i in range(N//2, 0, -1):
            if N % i == 0 and check(i):
                return True

        return False

print(Solution().repeatedSubstringPattern("abac"))                    
print(Solution().repeatedSubstringPattern("abab"))                    
print(Solution().repeatedSubstringPattern("aba"))                    
print(Solution().repeatedSubstringPattern("bb"))                    
print(Solution().repeatedSubstringPattern("abcabcabcabc"))                    

