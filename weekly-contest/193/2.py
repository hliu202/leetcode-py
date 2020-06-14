from util.common_imports import *

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        C = Counter(arr)
        L = []
        for key in C.keys():
            L.append(C[key])
        L.sort()
        i = 0
        while i < len(L) and k >= L[i]:
            k -= L[i]
            i += 1
        return len(L) - i

print(Solution().findLeastNumOfUniqueInts(arr = [1], k = 1))
print(Solution().findLeastNumOfUniqueInts(arr = [5,5,4], k = 1))
print(Solution().findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))