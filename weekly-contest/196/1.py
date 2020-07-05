from util.common_imports import *

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        x = arr[1]-arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != x:
                return False
        return True

print (Solution().canMakeArithmeticProgression([3,5,1]))
print (Solution().canMakeArithmeticProgression([4,2,1]))