
from util.common_imports import *

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)

        if k == N:
            return arr

        arr.sort()
        M = arr[(N-1)//2]
        res = []
        i = 0
        j = N -1

        def isIStrong(i_value, j_value):
            iv = abs(i_value - M)
            jv = abs(j_value - M)
            if iv > jv:
                return True
            elif iv == jv:
                return i_value > j_value
            else:
                return False

        while len(res) < k:
            if isIStrong(arr[i], arr[j]):
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
        return res

print(Solution().getStrongest(arr = [6,7,11,7,6,8], k = 5))
print(Solution().getStrongest(arr = [6,-3,7,2,11], k = 3))
print(Solution().getStrongest(arr = [-7,22,17,3], k = 2))
print(Solution().getStrongest(arr = [-2,-4,-6,-8,-9,-7,-5,-3,-1], k = 3))  # [-1,-9,-2]

