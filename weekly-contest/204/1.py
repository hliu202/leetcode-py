from util.common_imports import *

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if m*k > n: return False

        def check(idx):
            for j in range(0, m):
                for jj in range(1, k):
                    if arr[idx+j] != arr[idx+j+jj*m]:
                        return False
            return True

        for i in range(0, n - m*k + 1): # i为start的前m*k个，是否满足条件
            if check(i):
                return True
        return False

# print(Solution().containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3))
# print(Solution().containsPattern(arr = [1,2,1,2,1,1,1,3], m = 2, k = 2))
# print(Solution().containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3))
# print(Solution().containsPattern(arr = [1,2,3,1,2], m = 2, k = 2))
print(Solution().containsPattern(arr = [2,2], m = 1, k = 2)) # True
